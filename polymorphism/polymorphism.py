class CreditCard:
    def __init__(self, amount, currency) -> None:
        self.amount = amount
        self.currency = currency

    def process_payment(self, amount):
        print(f"Processing payment of {amount} {self.currency} with credit card")

class PayPal:
    def __init__(self, amount, currency) -> None:
        self.amount = amount
        self.currency = currency

    def process_payment(self, amount):
        print(f"Processing payment of {amount} {self.currency} with PayPal")

payment_method = CreditCard(100, "USD")
payment_method.process_payment(100)
payment_method2 = PayPal(150, "USD")
payment_method2.process_payment(150)

payment_methods = [
    CreditCard(200, "USD"),
    CreditCard(300, "USD"),
    PayPal(300, "EUR"),
    CreditCard(400, "GBP"),
    CreditCard(500, "JPY"),
    PayPal(200, "USD"),
    PayPal(400, "GBP")
]

for method in payment_methods:
    method.process_payment(200)