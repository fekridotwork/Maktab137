import re
from copy import deepcopy

def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (str(args), str(kwargs))
        if key in cache:
            print("\nWe had this in cache !\n")
            return deepcopy(cache[key])  
        result = func(*args, **kwargs)
        cache[key] = deepcopy(result)     
        return result
    return wrapper

@cache_decorator
def count_occur(Text: list, words: list):
    occurrence: dict = {}
    for word in Text:
        for wrd in words:
           if wrd == word:
                occurrence[wrd] = occurrence.get(wrd, 0) + 1
    return occurrence

# Getting input from the user
text: str = input("Please enter the sentence : ")
specific_words: str = (input
    ("Please enter words you want to count occurrence : "))

def cleaning_text(text: str):

    # accepting words and removing signs
    clean_text: list = re.findall(r'\b\w+\b', text)

    # lower casing all the chars for easier comparison
    lower_words = []
    lower_words = [word.lower() for word in clean_text]
    return lower_words

# Calling clean_text function 
clean_text = cleaning_text(text)
specific_words = cleaning_text(specific_words)

# Calling occur_dict for calculating occurrence of words
occur_dict = count_occur(clean_text, specific_words)

# Printing the result
for (key, value) in occur_dict.items():
    print(f"Occurrence of \"{key}\" in your sentence was <{value}> times.")

# Calling again to check saving in cache
occur_dict2 = count_occur(clean_text, specific_words)
for (key, value) in occur_dict2.items():
    print(f"Occurrence of \"{key}\" in your sentence was <{value}> times.")
