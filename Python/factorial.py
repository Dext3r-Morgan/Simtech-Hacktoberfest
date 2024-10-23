def factorial(n):
    # Check if n is a non-negative integer
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1  # 0! is defined as 1

    result = 1  # Initialize result to 1
    # Loop through all numbers from 1 to n
    for i in range(1, n + 1):
        result *= i  # Multiply result by i

    return result

def main():
    # Prompt user for input
    try:
        number = int(input("Enter a non-negative integer to find its factorial: "))
        fact = factorial(number)  # Call the factorial function
        print(f"The factorial of {number} is: {fact}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
