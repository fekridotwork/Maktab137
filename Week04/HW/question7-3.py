'''
:ماشین حساب ساده
تابعی بنویسید که دو عدد از نوع 
only-positional 
دریافت کند و 
عملگر
+ , - , *, / 
به صورت 
only-keyword
دریافت کند
سپس نتیجه را برگرداند

'''
def calculator(num1: int, num2: int, /, *, operator: str):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
        # If we want it always positive 
        # return abs(num1 - num2)
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
try:
    num1, num2 = map(float, input("Please enter your numbers: ").split())
    opr = input("Please enter the operator : ")
    result = calculator(num1, num2, operator = opr)
    print(f"The result of your operation is : {result}")
except ValueError:
    print("Invalid inputs!")