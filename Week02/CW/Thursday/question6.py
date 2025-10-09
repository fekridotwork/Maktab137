def palindrome(word):
    reversed_word = ""
    for ch in word:
        reversed_word = ch + reversed_word
    if word == reversed_word:
        return True
    else:
        return False    

word = input("Please enter the word : ")

if palindrome(word):
    print("Yes")
else:
    print("No")    
