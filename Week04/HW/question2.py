'''
ترکیب چند دکوراتور
:دو دکوراتور بنویسید
یکی ورودی های تابع را به استرینگ تبدیل کند
دیگری طول استرینگ هر ورودی را چاپ کند
بعد این دو را روی یک تابع با هم تست کنید 

'''
import ast

def string_cast(func):
    def wrapper(*args):
        new_args = tuple(str(a) for a in args)
        print("Stringed inputs".center(100, "-"))
        for x in new_args:
            print(f"Type \"{x}\" is {type(x)}")
        return func(*new_args)
    return wrapper

def len_input(func):
    def wrapper(*args):
        print("The length of each stringed input".center(100, "-"))
        for x in args:
            print(f"Length of \"{x}\" is : {len(x)}")
        return func(*args)
    return wrapper

@string_cast
@len_input
def test(*args):
    print("Running Main function".center(100, "-"))
    print("main function is running.")

input_values = input("Enter the function inputs : ").split()

converted_inputs = []

for val in input_values:
    try:
        converted_inputs.append(ast.literal_eval(val))
    except Exception:
        converted_inputs.append(val) 

print("Input values and their real type".center(100, "-"))
for val in converted_inputs:
    print(f"Type \"{val}\" is {type(val)}")  

test(*converted_inputs)