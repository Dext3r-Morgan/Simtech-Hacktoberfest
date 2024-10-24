def logistic(num, rate = 3.8765):
    num = rate * num * (1 - num)
    return num
 
if __name__ == "__main__":
    seed = float(input("Enter a number between 0 and 1: "))
    while seed <= 0 or seed >= 1:
        seed = float(input("Please enter a valid number between 0 and 1: "))
    count = int(input("Enter the number of random numbers to be generated: "))
    digits = int(input("Enter the degree of 10 for the range (type 0 for decimal numbers): "))
    for i in range(0,count):
        seed = logistic(seed)
        if digits == 0:
            print(seed)
 
        else:
            print(int(seed * (10 ** digits)))
