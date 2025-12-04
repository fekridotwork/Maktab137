class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Zero division!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        return self.history

calc = Calculator()

print(calc.add(4, 5))
print(calc.multiply(3, 7))
print(calc.divide(10, 2))

print("History:")
for h in calc.get_history():
    print(h)

