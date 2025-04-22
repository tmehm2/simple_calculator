def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
  if b != 0:
    return a / b
  else:
    return "Error: Division by zero"


def calculator():
    print("Welcome to calculator")
     
    operation = input("Choose operation: +, -, *, /: ")

    num1 = float(input("enter the first number "))
    num2 = float(input("enter the second number "))

    if operation == "+":
        print(f"the result is: {add(num1, num2)}")
    elif operation == "-":
        print(f"the result is {subtract(num1, num2)}")
    elif operation == "*":
        print(f"the result is {multiply(num1, num2)}")
    elif operation == "/":
        print(f"the result is {divide(num1, num2)}")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")


calculator()