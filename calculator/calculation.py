from abc import ABC, abstractmethod

class calculation(ABC):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    @abstractmethod
    def get_result(self):
        pass

class Add(calculation):
    def get_result(self):
        return self.a + self.b

class Subtract(calculation):
    def get_result(self):
        return self.a - self.b

class Multiply(calculation):
    def get_result(self):
        return self.a * self.b

class Divide(calculation):
    def get_result(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b