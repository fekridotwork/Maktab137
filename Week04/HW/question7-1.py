'''
تابعی که دو عدد دریافت می‌کند 
و جمع آن‌ها را برمی‌گرداند 
ورودی‌ها به صورت 
only positional 
تعریف شوند

'''
def sum_num (first_num, second_num, /):
    result = first_num + second_num
    return result

try:
    first_num, second_num = map(int, input("Please enter your numbers: ").split())
    result = sum_num(first_num, second_num)
    print(f"Sum of your numbers is : {result}")
except ValueError:
    print("Invalid Input!")