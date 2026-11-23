import re
import sqlite3
from datetime import date, datetime
from decimal import Decimal

import mysql.connector
from werkzeug.security import generate_password_hash

DB_FILE = "medistock.db"

sqlite3.register_adapter(Decimal, float)
sqlite3.register_adapter(date, lambda d: d.isoformat())


def _translate_sql(sql):
    sql = sql.replace("%s", "?")
    sql = re.sub(r"\bCURDATE\(\)", "date('now', 'localtime')", sql, flags=re.IGNORECASE)
    sql = re.sub(r"\bFOR UPDATE\b", "", sql, flags=re.IGNORECASE)
    return sql


def _convert_row(row):
    if row is None:
        return None
    result = dict(row)
    for key, val in result.items():
        if isinstance(val, str):
            if key in ("manufacturing_date", "expiry_date") and len(val) >= 10:
                try:
                    result[key] = date.fromisoformat(val[:10])
                except ValueError:
                    pass
            elif key == "created_at":
                try:
                    result[key] = datetime.fromisoformat(val)
                except ValueError:
                    pass
        elif key in ("unit_price", "inventory_value") and val is not None:
            result[key] = Decimal(str(val))
    return result


class _CursorWrapper:
    def __init__(self, cursor, dictionary=False):
        self._cursor = cursor
        self._dictionary = dictionary

    @property
    def lastrowid(self):
        return self._cursor.lastrowid

    def execute(self, sql, params=()):
        try:
            self._cursor.execute(_translate_sql(sql), params)
            return self
        except sqlite3.IntegrityError as err:
            raise mysql.connector.IntegrityError(str(err)) from err

    def fetchone(self):
        row = self._cursor.fetchone()
        if row is None:
            return None
        return _convert_row(row) if self._dictionary else tuple(row)

    def fetchall(self):
        rows = self._cursor.fetchall()
        return [_convert_row(r) if self._dictionary else tuple(r) for r in rows]

    def close(self):
        self._cursor.close()


class _ConnectionWrapper:
    def __init__(self, conn):
        self._conn = conn

    def cursor(self, dictionary=False):
        return _CursorWrapper(self._conn.cursor(), dictionary=dictionary)

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def close(self):
        self._conn.close()


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return _ConnectionWrapper(conn)


def init_pool(app=None):
    conn = sqlite3.connect(DB_FILE)
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            address TEXT NOT NULL,
            company_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            manufacturer TEXT NOT NULL,
            batch_number TEXT NOT NULL,
            manufacturing_date TEXT NOT NULL,
            expiry_date TEXT NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 0,
            unit_price REAL NOT NULL DEFAULT 0,
            supplier_id INTEGER REFERENCES suppliers(id) ON DELETE SET NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(name, batch_number)
        );

        CREATE TABLE IF NOT EXISTS stock_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine_id INTEGER,
            medicine_name TEXT NOT NULL,
            batch_number TEXT NOT NULL,
            movement TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            remarks TEXT,
            performed_by INTEGER REFERENCES users(id) ON DELETE SET NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    cur = conn.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        conn.execute(
            "INSERT INTO users (full_name, username, email, password_hash) VALUES (?, ?, ?, ?)",
            ("Admin User", "admin", "admin@medistock.local", generate_password_hash("admin123")),
        )
    conn.commit()
    conn.close()


def fetch_one(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute(sql, params)
        return cur.fetchone()
    finally:
        conn.close()


def fetch_all(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute(sql, params)
        return cur.fetchall()
    finally:
        conn.close()


def execute(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()