import hmac
import logging
import os
import re
import secrets
from datetime import date
from decimal import Decimal, InvalidOperation
from functools import wraps

import mysql.connector
from flask import Flask, abort, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from config import Config
from database import execute, fetch_all, fetch_one, get_connection, init_pool


CATEGORIES = ("Tablet", "Capsule", "Syrup", "Injection", "Ointment", "Other")
LOW_STOCK_THRESHOLD = 15
EMAIL_PATTERN = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
USERNAME_PATTERN = re.compile(r"[A-Za-z0-9_.-]{3,50}")


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    if not app.config["SECRET_KEY"]:
        raise RuntimeError("Set the SECRET_KEY environment variable before starting MediStock.")

    logging.basicConfig(level=logging.INFO)
    init_pool(app)

    @app.before_request
    def prepare_request():
        if "csrf_token" not in session:
            session["csrf_token"] = secrets.token_urlsafe(32)
        if request.method == "POST":
            submitted_token = request.form.get("csrf_token", "")
            if not hmac.compare_digest(session["csrf_token"], submitted_token):
                abort(400, description="Your form session expired. Please reload the page and try again.")
        g.user = None
        if session.get("user_id"):
            g.user = fetch_one(
                "SELECT id, full_name, username, email FROM users WHERE id = %s",
                (session["user_id"],),
            )
            if g.user is None:
                session.clear()
                session["csrf_token"] = secrets.token_urlsafe(32)

    @app.context_processor
    def inject_template_values():
        return {
            "csrf_token": session.get("csrf_token", ""),
            "today": date.today(),
            "low_stock_threshold": LOW_STOCK_THRESHOLD,
        }

    def login_required(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if g.user is None:
                flash("Please sign in to continue.", "error")
                return redirect(url_for("login"))
            return view(*args, **kwargs)

        return wrapped

    def form_text(name, label, maximum=150):
        value = request.form.get(name, "").strip()
        if not value:
            raise ValueError(f"{label} is required.")
        if len(value) > maximum:
            raise ValueError(f"{label} must be {maximum} characters or fewer.")
        return value

    def medicine_form_values():
        name = form_text("name", "Medicine name")
        category = form_text("category", "Category", 60)
        manufacturer = form_text("manufacturer", "Manufacturer")
        batch_number = form_text("batch_number", "Batch number", 80)
        if category not in CATEGORIES:
            raise ValueError("Choose a valid medicine category.")
        try:
            manufacturing_date = date.fromisoformat(request.form.get("manufacturing_date", ""))
            expiry_date = date.fromisoformat(request.form.get("expiry_date", ""))
            quantity = int(request.form.get("quantity", ""))
            unit_price = Decimal(request.form.get("unit_price", ""))
        except (TypeError, ValueError, InvalidOperation):
            raise ValueError("Enter valid dates, a whole-number quantity, and a valid price.")
        if expiry_date <= manufacturing_date:
            raise ValueError("Expiry date must be later than manufacturing date.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if (
            not unit_price.is_finite()
            or unit_price < 0
            or unit_price > Decimal("99999999.99")
            or unit_price.as_tuple().exponent < -2
        ):
            raise ValueError("Unit price must be between 0 and 99,999,999.99.")
        supplier_value = request.form.get("supplier_id", "").strip()
        try:
            supplier_id = int(supplier_value) if supplier_value else None
        except ValueError:
            raise ValueError("Choose a valid supplier.")
        if supplier_id is not None and not fetch_one("SELECT id FROM suppliers WHERE id = %s", (supplier_id,)):
            raise ValueError("The selected supplier no longer exists.")
        return (
            name,
            category,
            manufacturer,
            batch_number,
            manufacturing_date,
            expiry_date,
            quantity,
            unit_price,
            supplier_id,
        )

    def supplier_form_values():
        name = form_text("supplier_name", "Supplier name", 120)
        company = form_text("company_name", "Company name")
        phone = form_text("contact_number", "Contact number", 30)
        email = form_text("email", "Email address", 254).lower()
        address = form_text("address", "Address", 500)
        if not re.fullmatch(r"[+0-9() .-]{7,30}", phone) or not re.search(r"\d", phone):
            raise ValueError("Enter a valid contact number.")
        if not EMAIL_PATTERN.fullmatch(email):
            raise ValueError("Enter a valid email address.")
        return name, phone, email, address, company

    @app.route("/")
    def index():
        return redirect(url_for("dashboard") if g.user else url_for("login"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if g.user:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            user = fetch_one(
                "SELECT id, username, password_hash FROM users WHERE username = %s",
                (username,),
            )
            if user and check_password_hash(user["password_hash"], password):
                session.clear()
                session["user_id"] = user["id"]
                session["csrf_token"] = secrets.token_urlsafe(32)
                session.permanent = True
                flash("Welcome back. You are now signed in.", "success")
                return redirect(url_for("dashboard"))
            flash("Incorrect username or password.", "error")
        return render_template("login.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if g.user:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            try:
                full_name = form_text("full_name", "Full name", 120)
                username = form_text("username", "Username", 50)
                email = form_text("email", "Email address", 254).lower()
                password = request.form.get("password", "")
                if not USERNAME_PATTERN.fullmatch(username):
                    raise ValueError("Username must be 3-50 characters using letters, numbers, dots, dashes, or underscores.")
                if len(password) < 8:
                    raise ValueError("Password must contain at least 8 characters.")
                if len(password) > 128:
                    raise ValueError("Password must be 128 characters or fewer.")
                if not EMAIL_PATTERN.fullmatch(email):
                    raise ValueError("Enter a valid email address.")
                execute(
                    "INSERT INTO users (full_name, username, email, password_hash) VALUES (%s, %s, %s, %s)",
                    (full_name, username, email, generate_password_hash(password)),
                )
                flash("Your account is ready. Sign in to continue.", "success")
                return redirect(url_for("login"))
            except ValueError as error:
                flash(str(error), "error")
            except mysql.connector.IntegrityError:
                flash("That username or email address is already registered.", "error")
        return render_template("register.html")

    @app.post("/logout")
    @login_required
    def logout():
        session.clear()
        flash("You have been signed out.", "success")
        return redirect(url_for("login"))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        stats = fetch_one(
            """
            SELECT COUNT(*) AS total_medicines,
                   COALESCE(SUM(quantity), 0) AS total_stock,
                   COALESCE(SUM(quantity <= %s), 0) AS low_stock,
                   COALESCE(SUM(expiry_date < CURDATE()), 0) AS expired
            FROM medicines
            """,
            (LOW_STOCK_THRESHOLD,),
        )
        stats["total_suppliers"] = fetch_one("SELECT COUNT(*) AS count FROM suppliers")["count"]
        activities = fetch_all(
            """
            SELECT t.id, t.medicine_name, t.batch_number, t.movement, t.quantity,
                   t.remarks, t.created_at, u.full_name AS operator_name
            FROM stock_transactions t
            LEFT JOIN users u ON u.id = t.performed_by
            ORDER BY t.created_at DESC, t.id DESC LIMIT 10
            """
        )
        return render_template("dashboard.html", stats=stats, activities=activities)

    @app.get("/medicines")
    @login_required
    def medicines():
        search = request.args.get("q", "").strip()
        category = request.args.get("category", "").strip()
        if category and category not in CATEGORIES:
            abort(400, description="Choose a valid medicine category.")
        filters = []
        params = []
        if search:
            filters.append("(m.name LIKE %s OR m.batch_number LIKE %s OR m.manufacturer LIKE %s)")
            wildcard = f"%{search}%"
            params.extend((wildcard, wildcard, wildcard))
        if category in CATEGORIES:
            filters.append("m.category = %s")
            params.append(category)
        where = f"WHERE {' AND '.join(filters)}" if filters else ""
        rows = fetch_all(
            f"""
            SELECT m.*, s.supplier_name
            FROM medicines m LEFT JOIN suppliers s ON s.id = m.supplier_id
            {where} ORDER BY m.name, m.batch_number
            """,
            tuple(params),
        )
        return render_template(
            "medicines.html",
            medicines=rows,
            search=search,
            category=category,
            categories=CATEGORIES,
        )

    @app.route("/medicines/new", methods=["GET", "POST"])
    @login_required
    def add_medicine():
        suppliers = fetch_all("SELECT id, supplier_name, company_name FROM suppliers ORDER BY supplier_name")
        if request.method == "POST":
            try:
                values = medicine_form_values()
                connection = get_connection()
                cursor = None
                try:
                    cursor = connection.cursor()
                    cursor.execute(
                        """
                        INSERT INTO medicines
                            (name, category, manufacturer, batch_number, manufacturing_date,
                             expiry_date, quantity, unit_price, supplier_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        values,
                    )
                    medicine_id = cursor.lastrowid
                    if values[6] > 0:
                        cursor.execute(
                            """
                            INSERT INTO stock_transactions
                                (medicine_id, medicine_name, batch_number, movement, quantity, remarks, performed_by)
                            VALUES (%s, %s, %s, 'IN', %s, %s, %s)
                            """,
                            (medicine_id, values[0], values[3], values[6], "Initial stock", g.user["id"]),
                        )
                    connection.commit()
                except mysql.connector.Error:
                    connection.rollback()
                    raise
                finally:
                    if cursor is not None:
                        cursor.close()
                    connection.close()
                flash("Medicine batch added successfully.", "success")
                return redirect(url_for("medicines"))
            except ValueError as error:
                flash(str(error), "error")
            except mysql.connector.IntegrityError:
                flash("This medicine name and batch number are already registered.", "error")
        return render_template("add_medicine.html", medicine=None, suppliers=suppliers, categories=CATEGORIES)

    @app.route("/medicines/<int:medicine_id>/edit", methods=["GET", "POST"])
    @login_required
    def edit_medicine(medicine_id):
        medicine = fetch_one("SELECT * FROM medicines WHERE id = %s", (medicine_id,))
        if medicine is None:
            abort(404)
        suppliers = fetch_all("SELECT id, supplier_name, company_name FROM suppliers ORDER BY supplier_name")
        if request.method == "POST":
            try:
                values = medicine_form_values()
                connection = get_connection()
                cursor = None
                try:
                    cursor = connection.cursor(dictionary=True)
                    cursor.execute(
                        "SELECT name, batch_number, quantity FROM medicines WHERE id = %s FOR UPDATE",
                        (medicine_id,),
                    )
                    previous = cursor.fetchone()
                    if previous is None:
                        abort(404)
                    cursor.execute(
                        """
                        UPDATE medicines
                        SET name = %s, category = %s, manufacturer = %s, batch_number = %s,
                            manufacturing_date = %s, expiry_date = %s, quantity = %s,
                            unit_price = %s, supplier_id = %s
                        WHERE id = %s
                        """,
                        values + (medicine_id,),
                    )
                    quantity_delta = values[6] - previous["quantity"]
                    if quantity_delta:
                        cursor.execute(
                            """
                            INSERT INTO stock_transactions
                                (medicine_id, medicine_name, batch_number, movement, quantity, remarks, performed_by)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """,
                            (
                                medicine_id,
                                previous["name"],
                                previous["batch_number"],
                                "IN" if quantity_delta > 0 else "OUT",
                                abs(quantity_delta),
                                "Quantity adjusted via medicine edit",
                                g.user["id"],
                            ),
                        )
                    connection.commit()
                except mysql.connector.Error:
                    connection.rollback()
                    raise
                finally:
                    if cursor is not None:
                        cursor.close()
                    connection.close()
                flash("Medicine details updated successfully.", "success")
                return redirect(url_for("medicines"))
            except ValueError as error:
                flash(str(error), "error")
                medicine = dict(medicine)
                for key in ("name", "category", "manufacturer", "batch_number", "quantity", "unit_price", "supplier_id"):
                    if request.form.get(key) is not None:
                        medicine[key] = request.form.get(key)
            except mysql.connector.IntegrityError:
                flash("This medicine name and batch number are already registered.", "error")
        return render_template("add_medicine.html", medicine=medicine, suppliers=suppliers, categories=CATEGORIES)

    @app.post("/medicines/<int:medicine_id>/delete")
    @login_required
    def delete_medicine(medicine_id):
        if not fetch_one("SELECT id FROM medicines WHERE id = %s", (medicine_id,)):
            abort(404)
        execute("DELETE FROM medicines WHERE id = %s", (medicine_id,))
        flash("Medicine deleted. Its stock history has been retained.", "success")
        return redirect(url_for("medicines"))

    @app.route("/suppliers", methods=["GET", "POST"])
    @login_required
    def suppliers():
        if request.method == "POST":
            try:
                values = supplier_form_values()
                execute(
                    """
                    INSERT INTO suppliers (supplier_name, contact_number, email, address, company_name)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    values,
                )
                flash("Supplier added successfully.", "success")
                return redirect(url_for("suppliers"))
            except ValueError as error:
                flash(str(error), "error")
            except mysql.connector.IntegrityError:
                flash("A supplier with that email address already exists.", "error")
        rows = fetch_all(
            """
            SELECT s.*, COUNT(m.id) AS medicine_count
            FROM suppliers s LEFT JOIN medicines m ON m.supplier_id = s.id
            GROUP BY s.id ORDER BY s.supplier_name
            """
        )
        return render_template("suppliers.html", suppliers=rows, supplier=None)

    @app.route("/suppliers/<int:supplier_id>/edit", methods=["GET", "POST"])
    @login_required
    def edit_supplier(supplier_id):
        supplier = fetch_one("SELECT * FROM suppliers WHERE id = %s", (supplier_id,))
        if supplier is None:
            abort(404)
        if request.method == "POST":
            try:
                values = supplier_form_values()
                execute(
                    """
                    UPDATE suppliers SET supplier_name = %s, contact_number = %s, email = %s,
                        address = %s, company_name = %s WHERE id = %s
                    """,
                    values + (supplier_id,),
                )
                flash("Supplier details updated successfully.", "success")
                return redirect(url_for("suppliers"))
            except ValueError as error:
                flash(str(error), "error")
            except mysql.connector.IntegrityError:
                flash("A supplier with that email address already exists.", "error")
        rows = fetch_all(
            """
            SELECT s.*, COUNT(m.id) AS medicine_count
            FROM suppliers s LEFT JOIN medicines m ON m.supplier_id = s.id
            GROUP BY s.id ORDER BY s.supplier_name
            """
        )
        return render_template("suppliers.html", suppliers=rows, supplier=supplier)

    @app.post("/suppliers/<int:supplier_id>/delete")
    @login_required
    def delete_supplier(supplier_id):
        if not fetch_one("SELECT id FROM suppliers WHERE id = %s", (supplier_id,)):
            abort(404)
        execute("DELETE FROM suppliers WHERE id = %s", (supplier_id,))
        flash("Supplier deleted. Linked medicines are kept without a supplier.", "success")
        return redirect(url_for("suppliers"))

    @app.route("/stock", methods=["GET", "POST"])
    @login_required
    def stock():
        if request.method == "POST":
            try:
                medicine_id = int(request.form.get("medicine_id", ""))
                quantity = int(request.form.get("quantity", ""))
                movement = request.form.get("movement", "")
                remarks = request.form.get("remarks", "").strip()[:500]
                if movement not in ("IN", "OUT"):
                    raise ValueError("Choose stock received or stock distributed.")
                if quantity <= 0:
                    raise ValueError("Transaction quantity must be greater than zero.")
                connection = get_connection()
                cursor = None
                try:
                    cursor = connection.cursor(dictionary=True)
                    cursor.execute(
                        "SELECT id, name, batch_number, quantity FROM medicines WHERE id = %s FOR UPDATE",
                        (medicine_id,),
                    )
                    medicine = cursor.fetchone()
                    if medicine is None:
                        raise ValueError("Choose a medicine that still exists.")
                    if movement == "OUT" and quantity > medicine["quantity"]:
                        raise ValueError("There is not enough stock to complete this distribution.")
                    delta = quantity if movement == "IN" else -quantity
                    cursor.execute(
                        "UPDATE medicines SET quantity = quantity + %s WHERE id = %s",
                        (delta, medicine_id),
                    )
                    cursor.execute(
                        """
                        INSERT INTO stock_transactions
                            (medicine_id, medicine_name, batch_number, movement, quantity, remarks, performed_by)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            medicine_id,
                            medicine["name"],
                            medicine["batch_number"],
                            movement,
                            quantity,
                            remarks or None,
                            g.user["id"],
                        ),
                    )
                    connection.commit()
                except (mysql.connector.Error, ValueError):
                    connection.rollback()
                    raise
                finally:
                    if cursor is not None:
                        cursor.close()
                    connection.close()
                flash("Stock and transaction history updated.", "success")
                return redirect(url_for("stock"))
            except ValueError as error:
                flash(str(error), "error")
        medicines_list = fetch_all(
            "SELECT id, name, batch_number, quantity FROM medicines ORDER BY name, batch_number"
        )
        alerts = fetch_all(
            """
            SELECT id, name, batch_number, quantity, expiry_date
            FROM medicines
            WHERE quantity <= %s OR expiry_date < CURDATE()
            ORDER BY expiry_date, quantity
            """,
            (LOW_STOCK_THRESHOLD,),
        )
        transactions = fetch_all(
            """
            SELECT t.id, t.medicine_name, t.batch_number, t.movement, t.quantity,
                   t.remarks, t.created_at, u.full_name AS operator_name
            FROM stock_transactions t
            LEFT JOIN users u ON u.id = t.performed_by
            ORDER BY t.created_at DESC, t.id DESC LIMIT 100
            """
        )
        return render_template(
            "stock.html",
            medicines=medicines_list,
            alerts=alerts,
            transactions=transactions,
            low_stock_threshold=LOW_STOCK_THRESHOLD,
        )

    @app.get("/reports")
    @login_required
    def reports():
        overview = fetch_one(
            """
            SELECT COUNT(*) AS medicine_count, COALESCE(SUM(quantity), 0) AS total_units,
                   COALESCE(SUM(quantity * unit_price), 0) AS inventory_value,
                   COALESCE(SUM(quantity <= %s), 0) AS low_stock_count,
                   COALESCE(SUM(expiry_date < CURDATE()), 0) AS expired_count
            FROM medicines
            """,
            (LOW_STOCK_THRESHOLD,),
        )
        low_stock = fetch_all(
            "SELECT name, batch_number, quantity FROM medicines WHERE quantity <= %s ORDER BY quantity, name",
            (LOW_STOCK_THRESHOLD,),
        )
        expired = fetch_all(
            "SELECT name, batch_number, quantity, expiry_date FROM medicines WHERE expiry_date < CURDATE() ORDER BY expiry_date"
        )
        supplier_report = fetch_all(
            """
            SELECT s.supplier_name, s.company_name, s.contact_number, s.email, COUNT(m.id) AS medicine_count
            FROM suppliers s LEFT JOIN medicines m ON m.supplier_id = s.id
            GROUP BY s.id ORDER BY s.supplier_name
            """
        )
        transactions = fetch_all(
            """
            SELECT t.id, t.medicine_name, t.batch_number, t.movement, t.quantity,
                   t.remarks, t.created_at, u.full_name AS operator_name
            FROM stock_transactions t
            LEFT JOIN users u ON u.id = t.performed_by
            ORDER BY t.created_at DESC, t.id DESC LIMIT 100
            """
        )
        return render_template(
            "reports.html",
            overview=overview,
            low_stock=low_stock,
            expired=expired,
            suppliers=supplier_report,
            transactions=transactions,
            low_stock_threshold=LOW_STOCK_THRESHOLD,
        )

    @app.errorhandler(mysql.connector.Error)
    def handle_database_error(error):
        app.logger.error("A database operation failed: %s", error, exc_info=True)
        return render_template(
            "error.html",
            message="MediStock could not complete the database operation. Check your MySQL connection and try again.",
        ), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host=os.environ.get("FLASK_HOST", "127.0.0.1"),
        port=int(os.environ.get("FLASK_PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true",
    )
