from .BaseLogin import BaseLogin       
from utils.file_manager import load_data, save_data
class EmailLogin(BaseLogin):
    # Overriding Parent login method
    def login(self):
        
        users = load_data("Week09/HW/data/users.json")

        for attempt in range(1, 4):
            email = input("\nPlease enter your email : ").strip().lower()
            password = input("\nPlease enter your password : ").strip()

            is_valid = False
            for user in users:
                if user["email"].strip().lower() == email:
                    if user["password"] == password:
                        is_valid = True
                        break
                    else:
                        print(
                            "\nPassword you've entered is not valid! --> Try Again."
                            if attempt < 3
                            else "\nPassword you've entered is not valid! --> No more attempt left to try."
                            )
                        print(f"(Remaining attempts : {3 - attempt})")
                        break
            else:
                print(
                    "\nEmail you've entered is not valid! --> Try Again."
                    if attempt < 3
                    else "\nEmail you've entered is not valid! --> No more attempt left to try."
                    )
                print(f"(Remaining attempts : {3 - attempt})")
                continue
            if is_valid:
                print("\nYou've entered successfully!")
                break
            else:
                continue
        

