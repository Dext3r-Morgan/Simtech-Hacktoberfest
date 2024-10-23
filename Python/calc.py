# Function for the calculator
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "Invalid operation"

# Take user input for two numbers and an operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Call the calculator function and print the result
result = calculator(num1, num2, operation)
print("Result:", result)

