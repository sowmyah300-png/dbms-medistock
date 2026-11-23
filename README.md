# MediStock

A beginner-friendly Flask and MySQL medical inventory project. The working app uses MySQL for users, medicines, suppliers, and stock movement history. The existing `medistock_interactive_frontend_preview.html` is only a standalone visual preview; run the Flask application for database-backed functionality.

## Requirements

- Python 3.10 or newer
- MySQL Server 8.0.16+
- A terminal opened in this project folder

## 1. Create the database tables

Start MySQL Server, then open a terminal and run:

```powershell
Get-Content .\database.sql | mysql -u root -p
```

Enter your local MySQL password when prompted. If the `mysql` command is not on PATH, run the file from MySQL Workbench, or use the full path to `mysql.exe`.

## 2. Create a Python environment and install packages

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell prevents environment activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal and activate again.

## 3. Configure local connection settings

Set environment variables in the same PowerShell window used to run Flask. These values are not stored in the source files:

```powershell
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "your-local-mysql-password"
$env:MYSQL_DATABASE = "medistock"
$env:SECRET_KEY = (python -c "import secrets; print(secrets.token_hex(32))")
```

Use the MySQL account/password configured on your own computer. Do not commit credentials or the generated secret key.

## 4. Start and use MediStock

```powershell
python app.py
```

Open <http://127.0.0.1:5000>, choose **Create an account**, register the first operator, and sign in. MediStock does not include a shared default account or password.

## Project files

- `app.py` — Flask routes, authentication, validation, and inventory operations
- `database.py` — MySQL connection pool and parameterized query helpers
- `config.py` — environment-based configuration
- `database.sql` — database and table definitions with keys and relationships
- `templates/` — server-rendered login, dashboard, inventory, supplier, stock, report, and error pages
- `static/css/style.css` — responsive UI styling
- `static/js/script.js` — password visibility, confirmations, navigation, and print action

## Notes

- Passwords are stored as Werkzeug password hashes. All form submissions use session-bound CSRF tokens.
- Medicine batches are unique by medicine name and batch number. A supplier can be removed without deleting its medicine batches.
- Stock received and distributed is transactional: quantity updates and movement records commit together. Editing a batch quantity also creates a stock history record.
- Low stock is defined as 15 units or fewer. Change `LOW_STOCK_THRESHOLD` in `app.py` to adjust the rule.
- The Flask development server is intended for local college-project demonstrations, not production hosting.
