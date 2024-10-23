def sum_of_digits(number):
    total = 0  # Initialize total to 0
    while number > 0:
        digit = number % 10  # Extract the last digit
        total += digit  # Add the digit to the total
        number //= 10  # Remove the last digit from the number
    return total

def main():
    # Prompt user for input
    try:
        user_input = input("Enter a non-negative integer to calculate the sum of its digits: ")
        number = int(user_input)

        if number < 0:
            print("Please enter a non-negative integer.")
            return

        result = sum_of_digits(number)  # Call the sum_of_digits function
        print(f"The sum of the digits of {number} is: {result}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
