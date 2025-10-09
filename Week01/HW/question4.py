name = input("Please enter your name : ")
score = int(input("Please enter your score :"))

if score > 90:
    print(f"{name} : عالی")
elif score >= 70:
    print(f"{name} : خوب")
else:
    print(f"{name} : نیاز به پیشرفت")