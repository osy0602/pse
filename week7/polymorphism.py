class Payment:
    def make_payment(self):
        print("Payment methods")

class CreditCard(Payment):
    def make_payment(self):
            print("Credit card payment")

class PayPal(Payment):
    def make_payment(self):
            print("PayPal payment")
            
class BankTransfer(Payment):
    def make_payment(self):
            print("BankTransfer payment")

payments = [Payment(), CreditCard(), PayPal(), BankTransfer()]

for p in payments:
      p.make_payment()