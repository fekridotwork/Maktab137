'''
مقایسه رشته‌ها
در این تمرین, ۲ ورودی رشته ای با طول یکسان داریم 
خروجی تعداد تناقض های دو رشته به صورت نظیر به نظیر است
(حساس به حروف بزرگ و کوچک)
Input:
aBcD
ABcd
output: 2
'''
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

difference_count = 0

for char1, char2 in zip(first_string, second_string):
    if char1 != char2:
        difference_count += 1

print("Number of contradictions between two strings is : ", difference_count)
