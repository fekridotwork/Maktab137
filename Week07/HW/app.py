from utils.file_manager import load_data, save_data
from models.User import User

def signup():

    users = load_data("Week07/HW/data/users.json")

    while True:
        username = input("Enter username: ")
        duplicate = False
        for user in users:
            if user["username"] == username:
                print("Oops! This username already exists. Please choose another one.")
                duplicate = True
                break
        if not duplicate:
            break
    password = input("Enter your password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    birth_date = input("Enter birth date (YYYY-MM-DD): ")
    role = input("Enter role (admin / passenger): ")

    new_user = User(
            id = len(users) + 1,
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            birth_date = birth_date,
            created_at = None,
            role = role
        )
    
    # For Hashing
    new_user.set_password(password)

    users.append(new_user.to_dict())
    save_data("Week07/HW/data/users.json", users)

    print("User registered successfully!")

def login():
    users = load_data("Week07/HW/data/users.json")

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        user_found = None
        for user in users:
            if user["username"] == username:
                user_found = user
                break

        if user_found:
            temp_user = User(
                id=user_found["id"],
                username=user_found["username"],
                password=user_found["password"],
                first_name=user_found["first_name"],
                last_name=user_found["last_name"],
                phone=user_found["phone"],
                birth_date=user_found["birth_date"],
                created_at=user_found["created_at"],
                role=user_found["role"]
            )

            if temp_user.check_password(password):
                print(f"Login successful! Welcome {user_found['first_name']} {user_found['last_name']}\n")
                return user_found
            else:
                print("Incorrect password.\n")
        else:
            print("Username not found.\n")

        attempts += 1
        print(f"Attempts left: {max_attempts - attempts}\n")

    print("Too many failed attempts. Access denied.\n")
    return None

if __name__ == "__main__":
    print("1. Sign up")
    print("2. Login")
    choice = input("Choose: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
