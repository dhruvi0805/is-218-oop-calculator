class history:
    def __init__(self):
        self.history = []

    def add(self, calculation):
        self.history.append(calculation)

    def get_history(self):
        return list(self.history)

    def remove(self, calculation):
        self.history.remove(calculation)