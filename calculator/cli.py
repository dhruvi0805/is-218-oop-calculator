from calculator.calculation import Add, Subtract, Multiply, Divide
from calculator.history import History
import math

def run():
    history = History()

    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
    }

    while True:
        try: 
            command = input("Enter command: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting the calculator.")
            break

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
            try:
                number = int(input("Enter the number of the calculation to remove: "))
            except ValueError:
                print("Invalid removal number.")
            else:
                try:
                    removed = history.remove(number -1)
                except IndexError:
                    print("Calculation does not exist.")
                else:
                    print(f"Removed: {describe(removed)}")
            continue

        if command in operations:
            try: 
                a = float(input("Enter first number: "))
        
            except ValueError:
                print("Invalid number.")
                continue 

            if not math.isfinite(a):
                print("Number must be finite.")
                continue

            try: 
                b = float(input("Enter second number: "))

                operation = operations[command](a, b)
                result = operation.get_result()
            except ValueError:
                print("Invalid number or result.")
                continue

            if not math.isfinite(b):
                print("Number must be finite.")
                continue

            history.add(operation) 
            print(f"Result: {result:g}")

def describe(calculation):
    return f"{calculation.__class__.__name__}: {calculation.a:g},{calculation.b:g} ={calculation.get_result():g}"

def show_history(history):
    calculations = history.get_history()
    if not calculations: 
        print("No calculations in history.\n")
        return 
    
    for number, calculation in enumerate(history.get_history(), start=1):
        print(f"{number}. {describe(calculation)}")