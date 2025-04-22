def add(a, b):
    return a + b

print(add(4, 4))

def subtract(a, b):
    return a - b

print(subtract(4, 2))

def multiply(a, b):
    return a * b

print(multiply(3, 4))

def divide(a, b):
  if b != 0:
    return a / b
  else:
    return "Error: Division by zero"

print(divide(6, 0))

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