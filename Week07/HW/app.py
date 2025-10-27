from utils.file_manager import load_data, save_data
from models.User import User
from models.Travel import Travel

USERS_FILE = "Week07/HW/data/users.json"
TRAVELS_FILE = "Week07/HW/data/travels.json"


def signup():

    users = load_data(USERS_FILE)

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
            password = None,
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
    save_data(USERS_FILE, users)

    print("User registered successfully!")

def login():
    users = load_data(USERS_FILE)

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

def add_travel():

    travels = load_data(TRAVELS_FILE)

    origin = input("Please enter the origin : ")
    destination = input("Please enter the destination : ")
    departure_time = input("Please enter the departure time : ")
    duration = int(input("Please enter the duration of the trip : "))
    capacity = int(input("Please enter the seats capacity : "))
    price = float(input("Please enter the price : "))
                  
    new_travel = Travel(
        id = len(travels) + 1,
        origin = origin,
        destination = destination,
        departure_time = departure_time,
        duration = duration,
        capacity = capacity,
        available_seats = capacity,
        price = price,
        status = "active"
    )

    travels.append(new_travel.to_dict())
    save_data(TRAVELS_FILE, travels)

    print(f"Travel from {origin} to {destination} added successfully!\n")

def search_travels():

    travels = load_data(TRAVELS_FILE)

    origin = input("Enter origin (or leave empty): ").strip().lower()
    destination = input("Enter destination (or leave empty): ").strip().lower()
    date = input("Enter date (YYYY-MM-DD or leave empty): ").strip()

    results = [
        travel for travel in travels
        if (not origin or travel["origin"].lower() == origin)
        and (not destination or travel["destination"].lower() == destination)
        and (not date or travel["departure_time"].startswith(date))
    ]

    if not results:
        print("No travels found.")
        return

    print("\nSort results by:")
    print("1.Departure time")
    print("2.Price")
    print("3.Available seats")
    choice = input("Choose (1-3): ").strip()

    if choice == "1":
        results.sort(key=lambda t: t["departure_time"])
    elif choice == "2":
        results.sort(key=lambda t: t["price"])
    elif choice == "3":
        results.sort(key=lambda t: t["available_seats"], reverse=True)
    else:
        print("Invalid choice. Showing unsorted results.\n")

    print("\nSearch Results:")
    for travel in results:
        print(
            f"ID {travel['id']:>2} | {travel['origin']:<10} → {travel['destination']:<10} | "
            f"{travel['departure_time']:<19} | {travel['available_seats']:>2} | {travel['price']:>8.2f}"
        )


if __name__ == "__main__":
    print("1. Sign up")
    print("2. Login")
    choice = input("Choose: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
