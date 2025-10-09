from itertools import combinations
import re
import copy

# Getting input and export the words
text: str = input("Please enter your sentence : ")
words = re.findall(r'\b\w+\b', text)

# Defining the generator 
def combination_generator(word_list: list, n: int):
    for comb in combinations(word_list, n):
        yield list(comb)

# Defining the list of all combinations  
all_combs = []

# Printing the result 
print("")
for n in range(2, 5):
    print(f"The {n}-word combinations are : \n")
    for i in combination_generator(words, n):
        print(i)
        all_combs.append(i)
    print("")       

# Copy
print("The list of all combinations".center(105, '-'))
print("\n", all_combs, "\n") 

print("Shallow-copy of the main list".center(105, '-'))
shallow_copy_list = copy.copy(all_combs)
print("\n", shallow_copy_list, "\n")

print("Deep-copy of the main list".center(105, '-'))
deep_copy_list = copy.deepcopy(all_combs)
print("\n", deep_copy_list, "\n")

# Changing one element and see what happens in each copy
all_combs[0][0] = "maktab137"

print("The list of all combinations after change".center(105, '-'))
print("\n", all_combs , "\n") 

print("Shallow-copy of the main list after change".center(105, '-'))
print("\n", shallow_copy_list, "\n")

print("Deep-copy of the main list after change".center(105, '-'))
print("\n", deep_copy_list)
