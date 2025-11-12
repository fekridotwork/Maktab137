from authentication.EmailLogin import EmailLogin
from authentication.OTPLogin import OTPLogin
from authentication.GoogleLogin import GoogleLogin


LOGIN_METHODS = {
    "1": EmailLogin,
    "2": OTPLogin,
    "3": GoogleLogin
    }

while True:
    print("How do you want to Login ?")
    print("1. Email-Password")
    print("2. OTP")
    print("3. Google Login")
    print("Q. Quit")

    choice = input("Your choice: ").strip().lower()

    if choice == "q":
        print("Bye!")
        break

    if choice in LOGIN_METHODS:
        auth = LOGIN_METHODS[choice]()  
        auth.login()                    
        break
    else:
        print("Invalid Choice! --> Try Again.")