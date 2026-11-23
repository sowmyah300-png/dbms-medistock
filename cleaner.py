# The brain of the tool. Person 2 = find_issues, Person 3 = clean.
import re
import pandas as pd

EMAIL = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")


def phone_columns(df):
    return [c for c in df.columns if any(k in c.lower() for k in ("phone", "mobile", "contact"))]


def fix_phone(v):
    """Return None if the number is already a clean 10-digit Indian mobile number.
    Otherwise return (new_value, confidence); new_value is None if we cannot repair it."""
    s = str(v).strip()
    if s.endswith(".0"):
        s = s[:-2]
    if re.match(r"^[6-9]\d{9}$", s):
        return None
    digits = re.sub(r"[\s\-().]", "", s)
    if digits.startswith("+91"):
        digits = digits[3:]
    elif digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    elif digits.startswith("0") and len(digits) == 11:
        digits = digits[1:]
    if re.match(r"^[6-9]\d{9}$", digits):
        return (digits, "high")
    return (None, None)


def date_columns(df):
    return [c for c in df.columns if any(k in c.lower() for k in ("date", "joined", "dob"))]


def fix_date(v):
    """Return None if the date is already YYYY-MM-DD.
    Otherwise return (new_value, confidence). new_value is None if we cannot read it."""
    s = str(v).strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return None
    m = re.match(r"^(\d{1,2})[/-](\d{1,2})[/-](\d{4})$", s)
    if not m:
        return (None, None)
    a, b, year = int(m.group(1)), int(m.group(2)), m.group(3)
    if a > 12:
        day, month, conf = a, b, "high"      # clearly day first
    elif b > 12:
        day, month, conf = b, a, "high"      # clearly month first
    else:
        day, month, conf = a, b, "medium"    # could be either, we assume day first
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return (None, None)
    return (f"{year}-{month:02d}-{day:02d}", conf)


def dup_mask(df):
    """True for rows that repeat an earlier row. The 'id' column is ignored."""
    cols = [c for c in df.columns if c.lower() != "id"]
    return df.duplicated(subset=cols)


def find_issues(df):
    """Return a list of problems found. Nothing is changed here."""
    issues = []
    for col in df.columns:
        for i in df.index[df[col].isna()]:
            issues.append({"row": i, "column": col, "problem": "Missing value"})
    for i in df.index[dup_mask(df)]:
        issues.append({"row": i, "column": "(whole row)", "problem": "Duplicate row"})
    if "email" in df.columns:
        for i, v in df["email"].dropna().items():
            if not EMAIL.match(str(v)):
                issues.append({"row": i, "column": "email", "problem": "Invalid email format"})
    if "age" in df.columns:
        for i, v in df["age"].dropna().items():
            if v < 0 or v > 100:
                issues.append({"row": i, "column": "age", "problem": "Unlikely value (outlier)"})
    if "city" in df.columns:
        for i, v in df["city"].dropna().items():
            if v != v.strip().title():
                issues.append({"row": i, "column": "city", "problem": "Inconsistent spelling/case"})
    for col in date_columns(df):
        for i, v in df[col].dropna().items():
            if fix_date(v) is not None:
                issues.append({"row": i, "column": col, "problem": "Inconsistent date format"})
    for col in phone_columns(df):
        for i, v in df[col].dropna().items():
            result = fix_phone(v)
            if result is not None:
                kind = "Invalid phone number" if result[0] is None else "Inconsistent phone format"
                issues.append({"row": i, "column": col, "problem": kind})
    return pd.DataFrame(issues, columns=["row", "column", "problem"])


def quality_score(df):
    """Simple score: 100 = no problems."""
    total_cells = max(df.shape[0] * df.shape[1], 1)
    return round(100 * (1 - len(find_issues(df)) / total_cells), 1)


def clean(df):
    """Fix only what is safe. Return (clean_df, change_log, needs_review)."""
    df = df.copy()
    log, review = [], []

    def add(row, col, old, new, reason, conf):
        log.append({"row": row, "column": col, "old": old, "new": new,
                    "reason": reason, "confidence": conf})

    # 1) Remove exact duplicate rows (very safe)
    for i in df.index[dup_mask(df)]:
        add(i, "(whole row)", "duplicate row", "removed", "Same data as an earlier row (ignoring id)", "high")
    df = df[~dup_mask(df)]

    # 2) Fix city spelling/case (safe)
    if "city" in df.columns:
        for i, v in df["city"].dropna().items():
            new = v.strip().title()
            if new != v:
                df.at[i, "city"] = new
                add(i, "city", v, new, "Same city written in different style", "high")

    # 3) Fill missing age with the median (less sure -> medium)
    if "age" in df.columns:
        med = df["age"].median()
        for i in df.index[df["age"].isna()]:
            df.at[i, "age"] = med
            add(i, "age", "empty", med, "Filled with the median age of the column", "medium")

    # 4) Make dates look the same: YYYY-MM-DD
    for col in date_columns(df):
        for i, v in df[col].dropna().items():
            result = fix_date(v)
            if result is None:
                continue
            new, conf = result
            if new is None:
                review.append({"row": i, "column": col, "value": v,
                               "why": "Date format not understood"})
            else:
                df.at[i, col] = new
                why = "Date written in a different style"
                if conf == "medium":
                    why += " (day/month order is a guess: assumed day first)"
                add(i, col, v, new, why, conf)

    # 5) Phone numbers: tidy the format, flag the invalid ones
    for col in phone_columns(df):
        for i, v in df[col].items():
            if pd.isna(v):
                review.append({"row": i, "column": col, "value": "empty",
                               "why": "Cannot guess a missing phone number"})
                continue
            result = fix_phone(v)
            if result is None:
                continue
            new, conf = result
            if new is None:
                review.append({"row": i, "column": col, "value": v,
                               "why": "Not a valid 10-digit mobile number, correct value is unknown"})
            else:
                df.at[i, col] = new
                add(i, col, v, new, "Same number written with extra spaces, dashes or a country code", conf)

    # 6) Not sure -> do NOT change, only flag for a human
    for i, v in df.get("email", pd.Series(dtype=object)).dropna().items():
        if not EMAIL.match(str(v)):
            review.append({"row": i, "column": "email", "value": v,
                           "why": "Email looks invalid, correct value is unknown"})
    for i, v in df.get("age", pd.Series(dtype=float)).items():
        if v < 0 or v > 100:
            review.append({"row": i, "column": "age", "value": v,
                           "why": "Age looks unrealistic, correct value is unknown"})
    for i in df.index[df["city"].isna()] if "city" in df.columns else []:
        review.append({"row": i, "column": "city", "value": "empty",
                       "why": "Cannot guess a missing city safely"})

    return df, pd.DataFrame(log), pd.DataFrame(review)
