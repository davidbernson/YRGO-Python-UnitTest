class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise Exception("Not enough balance.")

    def apply_interest(self, interest):
        if isinstance(interest, (float, int)):
            self.balance = self.balance * (1 + (interest / 100))

    def get_balance(self):
        return self.balance
