import math


class Fibonacci:
    def __init__(self):
        pass

    def fibonacci_math(self, n):
        return 1/math.sqrt(5) * (((1 + math.sqrt(5)) / 2)**n - ((1 - math.sqrt(5)) / 2)**n)

    def fibonacci_recursive(self, n):
        if n in {0, 1}:
            return n
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)