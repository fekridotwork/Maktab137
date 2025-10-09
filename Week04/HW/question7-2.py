'''
تابعی که دو ورودی 
age , name 
دریافت می‌کند 
و چاپ می‌کند
ورودی‌ها از نوع 
only keyword
تعریف شوند

'''
def print_input(*, age: int, name: str):
    print(f"{name} is {age} years old.")
try:
    age, name = input("Please enter age and name : ").split()
    age = int(age)
    print_input(age = age , name = name)
except ValueError:
    print("Invalid Input!")
