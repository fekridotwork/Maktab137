'''
در این برنامه با استفاده از دیسکریپتور 
کنترل می‌کنیم که ویژگی 
score 
در کلاس 
Student 
همیشه عدد صحیح مثبت باشد
هر بار که مقدار 
score 
تغییر کند،
متد 
__set__ 
بررسی می‌کند
اگر مقدار منفی یا غیر عددی بود
، خطا 
(ValueError یا TypeError) 
می‌دهد.
اگر درست بود، مقدار در شیء ذخیره می‌شود.
'''
class PositiveInteger:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:   
            return self
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be integer!")
        if value <= 0:
            raise ValueError(f"{self.name} must be positive!")

        instance.__dict__[self.name] = value

class Student:

    score = PositiveInteger()  

    def __init__(self, score):
        self.score = score

ali = Student(18)
print(ali.score)   
ali.score = -5     
ali.score = "A"   

