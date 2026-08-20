from exchangeDB import create_connection
import sqlite3


class MoneyExchange:

    def register_customer(self, name, phone):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Customer (name, phone) VALUES (?, ?)",
            (name, phone)
        )

        conn.commit()
        conn.close()

        print(name+" registered successfully.")

    def view_customer(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Customer"
        )
        customers = cursor.fetchall()
        conn.close()
        return customers


    def register_currency(self, currency_code, currency_name):
        conn = create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """INSERT INTO Currency
                (currency_code, currency_name)
                VALUES (?, ?)""",
                (currency_code, currency_name)
            )

            conn.commit()
            print("Currency registered successfully.")

        except sqlite3.IntegrityError:
            print("Currency code already exists.")

        conn.close()

    def view_currency(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Currency"
        )
        currency = cursor.fetchall()
        conn.close()
        return currency

    def set_exchange_rate(self, from_currency, to_currency, rate):
        conn = create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """SELECT rate_id
                FROM ExchangeRate
                WHERE from_currency = ?
                AND to_currency = ?""",
                (from_currency, to_currency)
            )

            existing_rate = cursor.fetchone()

            if existing_rate:
                cursor.execute(
                    """UPDATE ExchangeRate
                    SET rate = ?
                    WHERE from_currency = ?
                    AND to_currency = ?""",
                    (rate, from_currency, to_currency)
                )

                print("Exchange rate updated successfully.")

            else:
                cursor.execute(
                    """INSERT INTO ExchangeRate
                    (from_currency, to_currency, rate)
                    VALUES (?, ?, ?)""",
                    (from_currency, to_currency, rate)
                )

                print("Exchange rate registered successfully.")

            conn.commit()

        except sqlite3.IntegrityError:
            print("Invalid currency code.")

        conn.close()

    def exchange_currency(
        self,
        customer_id,
        from_currency,
        to_currency,
        amount
    ):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(
            """SELECT rate
            FROM ExchangeRate
            WHERE from_currency = ?
            AND to_currency = ?""",
            (from_currency, to_currency)
        )

        result = cursor.fetchone()

        if result is None:
            print("Exchange rate not found.")
            conn.close()
            return

        exchange_rate = result[0]

        return_amount = amount * exchange_rate

        try:
            cursor.execute(
                """INSERT INTO ExchangeTransaction
                (
                    customer_id,
                    from_currency,
                    to_currency,
                    amount,
                    exchange_rate,
                    return_amount
                )
                VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    customer_id,
                    from_currency,
                    to_currency,
                    amount,
                    exchange_rate,
                    return_amount
                )
            )

            conn.commit()

            print(
                amount,
                from_currency,
                "is exchanged to",
                f"{return_amount:.2f}",
                to_currency
            )

        except sqlite3.IntegrityError:
            print("Invalid customer or currency information.")

        conn.close()


    def view_transactions(self):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT
                ExchangeTransaction.transaction_id,
                Customer.name,
                ExchangeTransaction.from_currency,
                ExchangeTransaction.to_currency,
                ExchangeTransaction.amount,
                ExchangeTransaction.exchange_rate,
                ExchangeTransaction.return_amount

            FROM ExchangeTransaction

            JOIN Customer
                ON ExchangeTransaction.customer_id
                = Customer.customer_id
        ''')

        rows = cursor.fetchall()
        conn.close()

        return rows
    
    def select_transactions_id(self, customer_id):
            conn = create_connection()
            cursor = conn.cursor()

            cursor.execute('''
                SELECT
                    ExchangeTransaction.transaction_id,
                    Customer.name,
                    ExchangeTransaction.from_currency,
                    ExchangeTransaction.to_currency,
                    ExchangeTransaction.amount,
                    ExchangeTransaction.exchange_rate,
                    ExchangeTransaction.return_amount

                FROM ExchangeTransaction

                JOIN Customer
                    ON ExchangeTransaction.customer_id
                    = Customer.customer_id
                WHERE ExchangeTransaction.customer_id = ?
            ''', (customer_id,))

            rows = cursor.fetchall()
            conn.close()

            return rows