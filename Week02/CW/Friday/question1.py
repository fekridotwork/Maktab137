# division and handle zeroDivisionError
numerator = float(input("Please enter the first number(numerator) : "))
denominator = float(input("Please enter the second number(denominator) : "))

try:
    result = numerator / denominator
    print("The result of this division is : ", result)
except ZeroDivisionError:
    print("Zero division is not acceptable !")
