from calculator.calculation import Add, Subtract, Multiply, Divide

def run():
    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide
    }

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            print("Exiting the calculator.")
            break

        if command == "help":
            print("Available commands: add, subtract, multiply, divide, help, exit")
            continue

        if command in operations:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            operation = operations[command](a, b)
            result = operation.get_result()
            print(f"Result: {result}")