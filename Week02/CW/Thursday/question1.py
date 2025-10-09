def shift(s):
    result = ""
    for char in s:
        result += chr(ord(char) + 1)
    return result

s = input("Please enter your string : ") 
print(shift(s)) 
