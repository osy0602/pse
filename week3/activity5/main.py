from exchangeDB import create_tables
from money_exchange import MoneyExchange


def menu():
    print("\n **************Money Exchange System****************")
    print("1. Register Customer")
    print("2. View Customers\n")

    print("3. Register Currency")
    print("4. View Currencies\n")

    print("5. Register / Update Exchange Rate")
    print("6. Exchange Currency\n")

    print("7. View All Exchange Transactions")
    print("8. View Customer Exchange Transactions\n")

    print("9. Exit")


def main():

    create_tables()

    exchange = MoneyExchange()

    while True:

        menu()

        choice = input("Select an option (1-9): ")

        if choice == '1':

            name = input("Enter customer name: ")
            phone = input("Enter phone number: ")

            exchange.register_customer(
                name,
                phone
            )

        elif choice == '2':
            customers_info = exchange.view_customer()
            for c in customers_info:
                print(c)

        elif choice == '3':

            currency_code = input(
                "Enter currency code (e.g. NZD): "
            ).upper()

            currency_name = input(
                "Enter currency name: "
            )

            exchange.register_currency(
                currency_code,
                currency_name
            )

        elif choice == '4':
            currency_info = exchange.view_currency()
            print("Present currencies:\n")
            for c in currency_info:
                print(c)

        elif choice == '5':

            from_currency = input(
                "From currency: "
            ).upper()

            to_currency = input(
                "To currency: "
            ).upper()

            rate = float(
                input("Enter exchange rate: ")
            )

            exchange.set_exchange_rate(
                from_currency,
                to_currency,
                rate
            )

        elif choice == '6':

            customer_id = int(
                input("Enter customer ID: ")
            )

            from_currency = input(
                "From currency: "
            ).upper()

            to_currency = input(
                "To currency: "
            ).upper()

            amount = float(
                input("Enter amount: ")
            )

            exchange.exchange_currency(
                customer_id,
                from_currency,
                to_currency,
                amount
            )


        elif choice == '7':

            transactions = exchange.view_transactions()

            for transaction in transactions:

                print(
                    "Transaction ID:", transaction[0],
                    "| Customer:", transaction[1],
                    "|", transaction[4], transaction[2],
                    "→",
                    transaction[6], transaction[3],
                    "| Rate:", transaction[5]
                )

        elif choice == '8':
            customer_id = int(input("Enter customer's customer id: "))
            customer_transaction = exchange.select_transactions_id(customer_id)
            for c in customer_transaction:
                print(c)

        elif choice == '9':

            print("Goodbye!")
            break


        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()