import sqlite3


def create_connection():
    conn = sqlite3.connect("MoneyExchange.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Currency (
            currency_code TEXT PRIMARY KEY,
            currency_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExchangeRate (
            rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_currency TEXT NOT NULL,
            to_currency TEXT NOT NULL,
            rate REAL NOT NULL,

            FOREIGN KEY (from_currency)
                REFERENCES Currency(currency_code),

            FOREIGN KEY (to_currency)
                REFERENCES Currency(currency_code),

            UNIQUE(from_currency, to_currency)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExchangeTransaction (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            from_currency TEXT NOT NULL,
            to_currency TEXT NOT NULL,
            amount REAL NOT NULL,
            exchange_rate REAL NOT NULL,
            return_amount REAL NOT NULL,

            FOREIGN KEY (customer_id)
                REFERENCES Customer(customer_id),

            FOREIGN KEY (from_currency)
                REFERENCES Currency(currency_code),

            FOREIGN KEY (to_currency)
                REFERENCES Currency(currency_code)
        )
    ''')

    conn.commit()
    conn.close()