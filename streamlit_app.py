from datetime import date
import os
import sqlite3
import pandas as pd
import streamlit as st
from werkzeug.security import check_password_hash, generate_password_hash

st.set_page_config(page_title="MediStock", page_icon="💊", layout="wide")

DB_PATH = "medistock.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_conn() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                username TEXT UNIQUE NOT NULL,
                email TEXT,
                password_hash TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_name TEXT NOT NULL,
                contact_number TEXT,
                email TEXT,
                address TEXT,
                company_name TEXT
            );
            CREATE TABLE IF NOT EXISTS medicines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                manufacturer TEXT,
                batch_number TEXT,
                manufacturing_date TEXT,
                expiry_date TEXT,
                quantity INTEGER DEFAULT 0,
                unit_price REAL DEFAULT 0.0,
                supplier_id INTEGER
            );
            CREATE TABLE IF NOT EXISTS stock_transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                medicine_id INTEGER,
                medicine_name TEXT,
                batch_number TEXT,
                movement TEXT,
                quantity INTEGER,
                remarks TEXT,
                performed_by INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        admin = conn.execute("SELECT id FROM users WHERE username = ?", ("admin",)).fetchone()
        if not admin:
            conn.execute(
                "INSERT INTO users (full_name, username, email, password_hash) VALUES (?, ?, ?, ?)",
                ("Administrator", "admin", "admin@medistock.local", generate_password_hash("admin123")),
            )
        conn.commit()


def fetch_all(query, params=()):
    with get_conn() as conn:
        rows = conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]


def fetch_one(query, params=()):
    with get_conn() as conn:
        row = conn.execute(query, params).fetchone()
        return dict(row) if row else None


def execute(query, params=()):
    with get_conn() as conn:
        conn.execute(query, params)
        conn.commit()


init_db()

if "user" not in st.session_state:
    st.session_state.user = None

# --- Authentication ---
if st.session_state.user is None:
    st.title("💊 MediStock — Medical Inventory System")
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="admin")
            password = st.text_input("Password", type="password", placeholder="admin123")
            if st.form_submit_button("Sign In"):
                user = fetch_one("SELECT * FROM users WHERE username = ?", (username.strip(),))
                if user and check_password_hash(user["password_hash"], password):
                    st.session_state.user = user
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

    with tab2:
        with st.form("register_form"):
            full_name = st.text_input("Full Name")
            new_user = st.text_input("Username")
            email = st.text_input("Email")
            new_pass = st.text_input("Password", type="password")
            if st.form_submit_button("Create Account"):
                if not full_name or not new_user or not new_pass:
                    st.warning("Full name, username, and password are required.")
                else:
                    try:
                        execute(
                            "INSERT INTO users (full_name, username, email, password_hash) VALUES (?, ?, ?, ?)",
                            (full_name.strip(), new_user.strip(), email.strip(), generate_password_hash(new_pass)),
                        )
                        st.success("Account created! Switch to the Login tab.")
                    except sqlite3.IntegrityError:
                        st.error("Username already exists.")
    st.stop()

# --- Sidebar ---
st.sidebar.title(f"👋 {st.session_state.user['full_name']}")
page = st.sidebar.radio("Navigation", ["Dashboard", "Medicines", "Stock In / Out", "Suppliers"])
if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.rerun()

# --- 1. Dashboard ---
if page == "Dashboard":
    st.header("Inventory Dashboard")
    meds = fetch_all("SELECT * FROM medicines")
    total_items = len(meds)
    total_units = sum(int(m["quantity"] or 0) for m in meds)
    total_val = sum(float(m["unit_price"] or 0) * int(m["quantity"] or 0) for m in meds)
    low_stock = sum(1 for m in meds if int(m["quantity"] or 0) <= 10)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Medicines", total_items)
    c2.metric("Total Stock Units", total_units)
    c3.metric("Inventory Value", f"₹{total_val:,.2f}")
    c4.metric("Low Stock Alerts", low_stock)

    st.subheader("Recent Stock Transactions")
    txns = fetch_all("SELECT * FROM stock_transactions ORDER BY id DESC LIMIT 10")
    if txns:
        st.dataframe(pd.DataFrame(txns), use_container_width=True)
    else:
        st.info("No stock transactions recorded yet.")

# --- 2. Medicines ---
elif page == "Medicines":
    st.header("Medicines & Batches")
    with st.expander("➕ Add New Medicine"):
        suppliers = fetch_all("SELECT id, supplier_name FROM suppliers")
        sup_map = {s["supplier_name"]: s["id"] for s in suppliers}
        with st.form("add_med"):
            col1, col2 = st.columns(2)
            name = col1.text_input("Medicine Name")
            category = col2.text_input("Category")
            manufacturer = col1.text_input("Manufacturer")
            batch = col2.text_input("Batch Number")
            mfg_date = col1.date_input("Manufacturing Date", value=date.today())
            exp_date = col2.date_input("Expiry Date", value=date.today())
            qty = col1.number_input("Initial Quantity", min_value=0, step=1)
            price = col2.number_input("Unit Price", min_value=0.0, step=0.5)
            sup_choice = st.selectbox("Supplier", ["None"] + list(sup_map.keys()))

            if st.form_submit_button("Save Medicine"):
                if not name.strip():
                    st.warning("Medicine Name is required.")
                else:
                    execute(
                        """INSERT INTO medicines (name, category, manufacturer, batch_number,
                           manufacturing_date, expiry_date, quantity, unit_price, supplier_id)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (
                            name.strip(),
                            category.strip(),
                            manufacturer.strip(),
                            batch.strip(),
                            str(mfg_date),
                            str(exp_date),
                            int(qty),
                            float(price),
                            sup_map.get(sup_choice),
                        ),
                    )
                    st.success("Medicine added!")
                    st.rerun()

    meds = fetch_all("SELECT * FROM medicines ORDER BY id DESC")
    if meds:
        st.dataframe(pd.DataFrame(meds), use_container_width=True)
    else:
        st.info("No medicines added yet.")

# --- 3. Stock In / Out ---
elif page == "Stock In / Out":
    st.header("Record Stock Movement")
    meds = fetch_all("SELECT id, name, batch_number, quantity FROM medicines")
    if not meds:
        st.info("Add medicines first before recording stock movements.")
    else:
        med_options = {
            f"{m['name']} (Batch: {m['batch_number'] or 'N/A'} | Qty: {m['quantity']})": m for m in meds
        }
        with st.form("stock_form"):
            selected_label = st.selectbox("Select Medicine", list(med_options.keys()))
            movement = st.radio("Movement Type", ["IN", "OUT"], horizontal=True)
            qty = st.number_input("Quantity", min_value=1, step=1)
            remarks = st.text_input("Remarks")
            if st.form_submit_button("Submit Transaction"):
                med = med_options[selected_label]
                current_qty = int(med["quantity"] or 0)
                if movement == "OUT" and qty > current_qty:
                    st.error("Insufficient stock available.")
                else:
                    new_qty = current_qty + int(qty) if movement == "IN" else current_qty - int(qty)
                    execute("UPDATE medicines SET quantity = ? WHERE id = ?", (new_qty, med["id"]))
                    execute(
                        """INSERT INTO stock_transactions
                           (medicine_id, medicine_name, batch_number, movement, quantity, remarks, performed_by)
                           VALUES (?, ?, ?, ?, ?, ?, ?)""",
                        (
                            med["id"],
                            med["name"],
                            med["batch_number"],
                            movement,
                            int(qty),
                            remarks.strip(),
                            st.session_state.user["id"],
                        ),
                    )
                    st.success("Stock updated!")
                    st.rerun()

# --- 4. Suppliers ---
elif page == "Suppliers":
    st.header("Supplier Directory")
    with st.expander("➕ Add Supplier"):
        with st.form("add_sup"):
            s_name = st.text_input("Contact Person")
            company = st.text_input("Company Name")
            phone = st.text_input("Contact Number")
            email = st.text_input("Email")
            address = st.text_area("Address")
            if st.form_submit_button("Save Supplier"):
                if not s_name.strip():
                    st.warning("Contact Person is required.")
                else:
                    execute(
                        "INSERT INTO suppliers (supplier_name, contact_number, email, address, company_name) VALUES (?, ?, ?, ?, ?)",
                        (s_name.strip(), phone.strip(), email.strip(), address.strip(), company.strip()),
                    )
                    st.success("Supplier added!")
                    st.rerun()

    sups = fetch_all("SELECT * FROM suppliers ORDER BY id DESC")
    if sups:
        st.dataframe(pd.DataFrame(sups), use_container_width=True)
    else:
        st.info("No suppliers added yet.")
        