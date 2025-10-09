def multiply(n, choice):
    def double(n):
        return n * 2
    def triple(n):
        return n * 3
    if choice == "double":
        return double(x)
    else:
        return triple(x)
    
x = int(input("Please enter your number : ")) 
choice = input("Please enter your choice : ") 
print("The result is : ", multiply(x, choice))
