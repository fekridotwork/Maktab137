n = int(input("Please enter your number : "))
i = 2
divisors = 1
while(i < n):
    if n % i == 0:
        divisors += i
    i += 1    
if divisors == n:
    print("Yes")
else :
    print("No")