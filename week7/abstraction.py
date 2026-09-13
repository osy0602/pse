from abc import ABC, abstractmethod

class ATM:
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class BankATM(ATM):

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def insert_card(self):
        print("Hello ", self.name)

    def enter_pin(self):
        if self.pin == int(input("enter your pin :")):
            return True
        else: 
            return False
        

    def check_balance(self):
        if self.enter_pin():
            print("here's your balance : $" + str(self.balance))
        else:
            print("Wrong Password")

    def withdraw(self, amount):
        if self.enter_pin():
            if self.balance < amount : 
                print("declined")
            else:
                print("Withdraw Accepted")
                print("Withdraw Money: $", str(amount))
                self.balance -= amount
                print("here's your balance : $" + str(self.balance))
        else:
            print("Wrong Password")

def main():
    a = BankATM("Maru",1234,3000)
    a.insert_card()
    while True:
        num = int(input("Select number(1: Check Balance, 2: Withdraw, 3: Exit): "))
        if num == 1:
            a.check_balance()
        elif num == 2:
            amount = int(input("withdraw amount: "))
            a.withdraw(amount)
        elif num == 3:
            break
        else:
            print("Invalid number, Try again")
            continue
if __name__ == "__main__":
    main()