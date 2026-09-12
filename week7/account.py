class Account:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Your present balance: ", self.balance)

    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print("You can't withdraw more than your balance")
        else:
            self.balance -= withdraw_amount
            print("Your present balance: ", self.balance)

class SavingsAccount(Account):
    """Calculate the interest earned based on their current balance and an interest rate"""

    def display(self):
        print("Account number: " ,self.account_number)
        print("Customer name: ",self.customer_name)
        print("Remaining balance: ", self.balance)
        """interest at a rate of 5 percent"""
        print("interest at a rate of 5 percent: ", round(self.balance * 0.05, 2))

def main():
    johns_saving_account = SavingsAccount('SA1001','John',5000)
    johns_saving_account.deposit(1000)
    johns_saving_account.withdraw(500)
    johns_saving_account.display()


if __name__ == "__main__":
    main()