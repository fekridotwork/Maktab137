'''
درمورد دکوراتور با 3 فانکشن جستجو کنید 
و سپس دکوراتوری بنویسید که 
تابع مورد نظر را فقط در محدوده
زمانی مشخصی اجرا کند 

'''
from datetime import datetime

def restrict_hours(start, end):         
    def decorator(func):               
        def wrapper(*args, **kwargs):   
            print(args, kwargs)
            hour = datetime.now().hour
            if start <= hour < end:
                print(f"Current hour is {hour} in the allowed duration!")
                return func(*args, **kwargs)
            else:
                print(f"It's {hour} now and It's not in the allowed duration!")
        return wrapper
    return decorator

@restrict_hours(start = 9, end = 17)
def do_work(y, x):
    print("Working...")

do_work(3 , x = 5)
