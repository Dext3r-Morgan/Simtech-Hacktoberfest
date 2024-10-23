# Function to calculate the sum of digits of a number
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10  # Add the last digit to the total
        num = num // 10    # Remove the last digit
    return total

# Take user input for the number
num = int(input("Enter a number: "))

# Call the function and print the result
print("Sum of digits:", sum_of_digits(num))
