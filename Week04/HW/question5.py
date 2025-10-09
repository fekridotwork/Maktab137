'''
دکوراتوری که 
ورودی یک تابع را در فایل 
txt.input 
و خروجی تابع را در فایل 
txt.output 
بنویسد

'''
def file_io(input_file, output_file):
    def decorator(func):
        def wrapper(data):

            with open(input_file, 'w', encoding='utf-8') as file:
                file.write(data)

            result = func(data)

            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(result)

            return result
        return wrapper
    return decorator


@file_io(input_file='input.txt', output_file='output.txt')
def process_data(data):
    return data.upper()

data = input("Please enter the data : ")
process_data(data)
