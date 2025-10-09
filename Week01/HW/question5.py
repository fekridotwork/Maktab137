n = 6

# Calculating factorial of 6 with for
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of 6 using for is : {factorial}")

# Calculating factorial of 6 with while
factorial = 1
i = 1
while i <= n :
    factorial *= i
    i += 1
print(f"Factorial of 6 using while is : {factorial}")    