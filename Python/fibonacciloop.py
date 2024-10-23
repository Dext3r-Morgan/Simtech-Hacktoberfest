# Function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by the current number
    return result

# Take user input for the number
n = int(input("Enter a number: "))

# Call the function and print the factorial
print(f"Factorial of {n} is:", factorial(n))
