from datetime import date
import pandas as pd
import streamlit as st
from werkzeug.security import check_password_hash, generate_password_hash
import database as db

st.set_page_config(page_title="MediStock", page_icon="💊", layout="wide")
db.init_pool()

if "user" not in st.session_state:
    st.session_state.user = None

# --- Login / Register ---
if st.session_state.user is None:
    st.title("💊 MediStock — Medical Inventory System")
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Sign In"):
                user = db.fetch_one("SELECT * FROM users WHERE username = %s", (username,))
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
                try:
                    db.execute(
                        "INSERT INTO users (full_name, username, email, password_hash) VALUES (%s, %s, %s, %s)",
                        (full_name, new_user, email, generate_password_hash(new_pass)),
                    )
                    st.success("Account created! Switch to the Login tab.")
                except Exception as e:
                    st.error(f"Registration failed: {e}")
    st.stop()

# --- Sidebar Navigation ---
st.sidebar.title(f"👋 {st.session_state.user['full_name']}")
page = st.sidebar.radio("Navigation", ["Dashboard", "Medicines", "Stock In / Out", "Suppliers"])
if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.rerun()

# --- 1. Dashboard ---
if page == "Dashboard":
    st.header("Inventory Dashboard")
    meds = db.fetch_all("SELECT * FROM medicines")
    total_items = len(meds)
    total_units = sum(m["quantity"] for m in meds)
    total_val = sum(float(m["unit_price"]) * m["quantity"] for m in meds)
    low_stock = sum(1 for m in meds if m["quantity"] <= 10)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Medicines", total_items)
    c2.metric("Total Stock Units", total_units)
    c3.metric("Inventory Value", f"₹{total_val:,.2f}")
    c4.metric("Low Stock Alerts", low_stock)

    st.subheader("Recent Stock Transactions")
    txns = db.fetch_all("SELECT * FROM stock_transactions ORDER BY id DESC LIMIT 10")
    st.dataframe(pd.DataFrame(txns), use_container_width=True)

# --- 2. Medicines ---
elif page == "Medicines":
    st.header("Medicines & Batches")
    with st.expander("➕ Add New Medicine"):
        suppliers = db.fetch_all("SELECT id, supplier_name FROM suppliers")
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
                db.execute(
                    """INSERT INTO medicines (name, category, manufacturer, batch_number,
                       manufacturing_date, expiry_date, quantity, unit_price, supplier_id)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (name, category, manufacturer, batch, mfg_date, exp_date, qty, price, sup_map.get(sup_choice)),
                )
                st.success("Medicine added!")
                st.rerun()

    meds = db.fetch_all("SELECT * FROM medicines ORDER BY id DESC")
    st.dataframe(pd.DataFrame(meds), use_container_width=True)

# --- 3. Stock Movements ---
elif page == "Stock In / Out":
    st.header("Record Stock Movement")
    meds = db.fetch_all("SELECT id, name, batch_number, quantity FROM medicines")
    if not meds:
        st.info("Add medicines first before recording stock movements.")
    else:
        med_options = {f"{m['name']} (Batch: {m['batch_number']} | Qty: {m['quantity']})": m for m in meds}
        with st.form("stock_form"):
            selected_label = st.selectbox("Select Medicine", list(med_options.keys()))
            movement = st.radio("Movement Type", ["IN", "OUT"], horizontal=True)
            qty = st.number_input("Quantity", min_value=1, step=1)
            remarks = st.text_input("Remarks")
            if st.form_submit_button("Submit Transaction"):
                med = med_options[selected_label]
                if movement == "OUT" and qty > med["quantity"]:
                    st.error("Insufficient stock available.")
                else:
                    new_qty = med["quantity"] + qty if movement == "IN" else med["quantity"] - qty
                    db.execute("UPDATE medicines SET quantity = %s WHERE id = %s", (new_qty, med["id"]))
                    db.execute(
                        """INSERT INTO stock_transactions
                           (medicine_id, medicine_name, batch_number, movement, quantity, remarks, performed_by)
                           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                        (med["id"], med["name"], med["batch_number"], movement, qty, remarks, st.session_state.user["id"]),
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
                db.execute(
                    "INSERT INTO suppliers (supplier_name, contact_number, email, address, company_name) VALUES (%s, %s, %s, %s, %s)",
                    (s_name, phone, email, address, company),
                )
                st.success("Supplier added!")
                st.rerun()

    sups = db.fetch_all("SELECT * FROM suppliers ORDER BY id DESC")
    st.dataframe(pd.DataFrame(sups), use_container_width=True)