# commands.py

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")

def add():
    print("Addition")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print(f"Result: {a} + {b} = {a + b}")

def subtract():
    print("Subtraction")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print(f"Result: {a} - {b} = {a - b}")

def multiply():
    print("Multiplication")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print(f"Result: {a} * {b} = {a * b}")

def divide():
    print("Division")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return
    print(f"Result: {a} / {b} = {a / b}")

# Dictionary for dynamic command lookup
command_dict = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}
