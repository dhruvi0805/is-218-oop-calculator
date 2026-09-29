class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        return self.a +self.b

class Subtract:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        return self.a - self.b

class Multiply:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        return self.a * self.b

class Divide:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b