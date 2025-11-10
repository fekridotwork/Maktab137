import BaseLogin
from utils.file_manager import load_data, save_data


class EmailLogin(BaseLogin):
    # Overriding Parent login method
    def login(self):
        
        users = load_data("data/users.json")

        while True: # Adding Limit for attempts
            email = input("Please enter your email : ").strip().lower()
            password = input("Please enter your password : ").strip()

            is_valid = False
            for user in users:
                if user["email"] == email:
                    if user["password"] == password:
                        is_valid = True
                        break
                    else:
                        print("Password you've entered is not valid! --> Try Again.")
            else:
                print("Email you've entered is not valid! --> Try Again.")
                continue
            if is_valid:
                print("You've entered successfully!")
                break
        

