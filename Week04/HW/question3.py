'''
تابعی بنویسید که یک لیست بگیرد و 
عنصری که بیشترین تکرار را دارد برگرداند

'''

def occurrence (input_list : list) -> str:

    occur_dict = {}

    # Storing counts of each item appearance
    for element in input_list:
        occur_dict[element] = occur_dict.get(element, 0) + 1

    # finding the max occurrence
    max_occur = max(occur_dict.values())

    # Finding all max_occur elements
    result = [k for k, v in occur_dict.items() if v == max_occur]
    return result


input_list = [x.lower() for x in input("Please enter your list : ").split()]
#input_list = "Ali ali matin amir ali matin matin ali Amir"

result = occurrence(input_list)
print("Most frequent element is :", result)
