# calculator.py

def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    op = input("Choose operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation."

    return f"Result: {result}"

print(calculator())
