class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise Exception("Not enough balance.")

    def apply_interest(self, interest):
        if isinstance(interest, (float, int)):
            self._balance = self._balance * (1 + (interest / 100))

    def get_balance(self):
        return self._balance
