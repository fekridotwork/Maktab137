from .BaseLogin import BaseLogin  
from utils.file_manager import load_data, save_data

class GoogleLogin(BaseLogin):
    # Overriding Parent login method
    def login(self):

        google_users = load_data("Week09/HW/data/google_users.json")

        for user in google_users:

            if user["is_login"] == True:

                while True:

                    print("\nDo you want to continue with this google account?")
                    print(f"Username : {user['username']} | email : {user['email']}")
                    choice = input("Your choice (y/n) : ").lower()
                    if choice == "y":
                        print("\nSo you are already logged in!")
                        return
                    
                    elif choice == "n":
                        user["is_login"] = False
                        save_data("Week09/HW/data/google_users.json", google_users)
                        break

                    else:
                        print("\nInvalid choice! --> Try Again.")
                break

        email = input("\nPlease enter your google account email : ").strip().lower()

        for user in google_users:

            if user["email"].strip().lower() == email:

                for attempt in range(1, 4):

                    password = input("\nNow enter your password : ")

                    if password == user["password"]:
                        user["is_login"] = True
                        save_data("Week09/HW/data/google_users.json", google_users)
                        print("\nYou've entered your google account successfully!")
                        return
                    
                    else:
                        print("\nWrong Password! --> Try Again.")
                        print(f"Remaining attempts : {3 - attempt}")

                print("\nNo more attempt is allowed! --> Try another way.")
                return
            
        print("\nYour email wasn't found in the system! --> Try another way.")
            
