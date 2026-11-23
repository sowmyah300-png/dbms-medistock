
import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "medistock-local-development-key-2026"
    )

    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.environ.get("MYSQL_PORT", "3306"))
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "medistock")

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.environ.get(
        "COOKIE_SECURE", "false"
    ).lower() == "true"

    PERMANENT_SESSION_LIFETIME = timedelta(hours=8)
