num = float(input("Please enter an integer number : "))

try:
    int_num = int(num)
    print("This is the integer part of your number :", int_num)
except ValueError:
    print("Your input is not a number !")