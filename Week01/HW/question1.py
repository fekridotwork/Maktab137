input_list: list = list(input("Please enter the string : "))
   
for i in range(len(input_list)-1, -1, -1):
    if input_list[i] == ' ':
        del input_list[i]
    elif input_list[i] in 'aeiou':
        input_list[i] = '.'

   
for i in range(len(input_list)-1, -1, -1) :
    print(input_list[i], end = '')  