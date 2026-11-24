def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ").strip()
    if operation == "+":
        answer = add(first, second)
    elif operation == "-":
        answer = subtract(first, second)
    elif operation == "*":
        answer = multiply(first, second)
    elif operation == "/":
        answer = divide(first, second)
    else:
        print("Sorry, please choose +, -, * or /.")
        answer = None
    if answer is not None:
        print(f"Your answer is {answer}. Nice work!")
except ValueError:
    print("Please enter numbers for the first and second values.")
except ZeroDivisionError:
    print("You can't divide by zero. Please try another number.")