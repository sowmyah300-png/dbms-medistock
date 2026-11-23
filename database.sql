CREATE DATABASE IF NOT EXISTS medistock
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE medistock;

CREATE TABLE IF NOT EXISTS users (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(120) NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(254) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_users_username (username),
    UNIQUE KEY uq_users_email (email)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS suppliers (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    supplier_name VARCHAR(120) NOT NULL,
    contact_number VARCHAR(30) NOT NULL,
    email VARCHAR(254) NOT NULL,
    address VARCHAR(500) NOT NULL,
    company_name VARCHAR(150) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_suppliers_email (email)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS medicines (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(60) NOT NULL,
    manufacturer VARCHAR(150) NOT NULL,
    batch_number VARCHAR(80) NOT NULL,
    manufacturing_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    quantity INT UNSIGNED NOT NULL DEFAULT 0,
    unit_price DECIMAL(10, 2) UNSIGNED NOT NULL,
    supplier_id INT UNSIGNED NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_medicine_batch (name, batch_number),
    KEY idx_medicines_expiry (expiry_date),
    KEY idx_medicines_category (category),
    CONSTRAINT fk_medicines_supplier
        FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    CONSTRAINT chk_medicines_dates CHECK (expiry_date > manufacturing_date)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS stock_transactions (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    medicine_id INT UNSIGNED NULL,
    medicine_name VARCHAR(150) NOT NULL,
    batch_number VARCHAR(80) NOT NULL,
    movement ENUM('IN', 'OUT') NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    remarks VARCHAR(500) NULL,
    performed_by INT UNSIGNED NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_stock_transactions_created (created_at),
    KEY idx_stock_transactions_medicine (medicine_id),
    CONSTRAINT fk_transactions_medicine
        FOREIGN KEY (medicine_id) REFERENCES medicines (id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    CONSTRAINT fk_transactions_user
        FOREIGN KEY (performed_by) REFERENCES users (id)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;
