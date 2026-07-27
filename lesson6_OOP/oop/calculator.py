class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self.result

    def reset(self):
        self.result = 0
        return self.result

calc1 = Calculator()
print(calc1.add(5))
print(calc1.add(10))
calc1.reset()
print(calc1.result)