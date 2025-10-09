'''
برنامه‌ای بنویسید که با استفاده از تابعی بازگشتی 
عناصر یک لیست تو در تو را جمع کند

'''
import ast
def nested_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):   
            print(f"Going into: {element}")
            total += nested_sum(element)  
        else:
            print(f"Adding: {element}")
            total += element   
    return total

#print(nested_sum([1, [2, 3], [4, [5]]])) 

user_input = input("Enter a nested list : ")
nested_list = ast.literal_eval(user_input) 

print("Sum =", nested_sum(nested_list))

