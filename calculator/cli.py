from calculator.calculation import Add, Subtract, Multiply, Divide
from calculator.history import History

def run():
    history = History()

    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
    }

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            print("Exiting the calculator.")
            break

        if command == "help":
            print("Available commands: add, subtract, multiply, divide, help, exit")
            continue

        if command == "history":
            show_history(history)
            continue

        if command == "remove":
            number = int(input("Enter the number of the calculation to remove: "))
            history.remove(number - 1)  # Convert to zero-based index
            continue

        if command in operations:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            operation = operations[command](a, b)
            history.add(operation)

            result = operation.get_result()
            print(f"Result: {result}")

def describe(calculation):
    return f"{calculation.get_result():g}"

def show_history(history):
    for number, calculation in enumerate(history.get_history(), start=1):
        print(f"{number}.{describe(calculation)}")