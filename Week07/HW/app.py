from utils.file_manager import load_data, save_data
from datetime import datetime
from models.User import User
from models.Travel import Travel
from models.Ticket import Ticket
from models.Payment import Payment

USERS_FILE = "Week07/HW/data/users.json"
TRAVELS_FILE = "Week07/HW/data/travels.json"
TICKETS_FILE = "Week07/HW/data/tickets.json"
PAYMENTS_FILE = "Week07/HW/data/payments.json"


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
    # Only Admin can do this

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

def reserve_ticket():

    travels = load_data(TRAVELS_FILE)

    try:
        travel_id = int(input("Please enter the travel ID : "))
    except ValueError:
        print("Travel_ID you entered is not valid!")
        # Getting another id?
        return

    travel = next((t for t in travels if t["id"] == travel_id), None)

    # When we didn't find any travel with that ID
    if not travel:
        print("Travel not found.")
        # getting another travel id?
        return
    
    # Checking that this travel has available seats or not
    if travel["available_seats"] <= 0:
        print("No seats available for this travel.")
        # getting another travel id?
        return
    
    # Specifying a seat number for the user \ could be improved
    seat_number = travel["capacity"] - travel["available_seats"] + 1

    tickets = load_data(TICKETS_FILE)
    new_ticket = Ticket(
        id = len(tickets) + 1,
        user_id = 1, # Not specified
        travel_id = travel["id"],
        seat_number = seat_number,
        status = "reserved",
        created_at = str(datetime.now())
    )

    travel["available_seats"] -= 1

    tickets.append(new_ticket.to_dict())
    save_data(TICKETS_FILE, tickets)
    save_data(TRAVELS_FILE, travels)

    print(f"\nTicket reserved successfully!")
    print(f"Travel: {travel['origin']} -> {travel['destination']} on {travel['departure_time']}")
    print(f"Seat number: {seat_number}")

def make_payment(user):

    tickets = load_data(TICKETS_FILE)
    travels = load_data(TRAVELS_FILE)
    payments = load_data(PAYMENTS_FILE)

    ticket_id = int(input("Enter your ticket ID to pay: ").strip())

    ticket = next((ticket for ticket in tickets if ticket["id"] == ticket_id), None)

    if not ticket:
        print("Ticket not found.")
        return
    
    if ticket["user_id"] != user["id"]:
        print("This ticket does not belong to you.")
        return

    if ticket["status"] != "reserved":
        print("This ticket is already paid or cancelled.")
        return

    travel = next((travel for travel in travels if travel["id"] == ticket["travel_id"]), None)

    if not travel:
        print("Travel not found for this ticket.")
        return
    
    amount = travel["price"]

    new_payment = Payment(
        id = len(payments) + 1,
        user_id = user["id"],
        ticket_id = ticket["id"],
        amount = amount,
        status = "success",
        paid_at = str(datetime.now())
    )

    ticket["status"] = "paid"

    payments.append(new_payment.to_dict())
    save_data(PAYMENTS_FILE, payments)
    save_data(TICKETS_FILE, tickets)

    print("\nPayment successful!")
    print(f"Ticket ID: {ticket['id']}")
    print(f"Amount Paid: {amount:.2f}")
    print(f"Time: {new_payment.paid_at}")

def edit_travel():
    # For admin only
    
    travels = load_data(TRAVELS_FILE)
    if not travels:
        print("No travels to edit.")
        return
    
    try:
        travel_id = int(input("Please enter the travel id: ").strip())
    except ValueError:
        print("Invalid travel ID.")
        return
    
    target_travel = None
    for travel in travels:
        if travel_id == travel["id"]:
            target_travel = travel
            break

    if not target_travel:
        print("Your target travel didn't found.")
        # Getting id again?
        return
    
    while True:
        print("\n--- Current travel ---")
        print(f"ID: {target_travel['id']}")
        print(f"1) origin         : {target_travel['origin']}")
        print(f"2) destination    : {target_travel['destination']}")
        print(f"3) departure_time : {target_travel['departure_time']}")
        print(f"4) duration       : {target_travel['duration']} (minutes)")
        print(f"5) capacity       : {target_travel['capacity']}")
        print(f"6) available_seats: {target_travel['available_seats']}")
        print(f"7) price          : {target_travel['price']}")
        print(f"8) status         : {target_travel['status']}")
        print("9) SAVE changes")
        print("0) CANCEL (discard changes)")

        option = input("\nChoose field to edit (0..9): ")

        if option == "0":
            print("Changes discarded.")
            return
        
        elif option == "1":
            origin = input("Please enter the new origin : ").strip()
            if origin:
                target_travel["origin"] = origin
            else:
                print("No Change.")

        elif option == "2":
            destination = input("Please enter the new destination : ").strip()
            if destination:
                target_travel["destination"] = destination
            else:
                print("No Change.")

        elif option == "3":
            departure_time = input("Please enter the new departure_time : ").strip()
            if departure_time:
                target_travel["departure_time"] = departure_time
            else:
                print("No Change.")

        elif option == "4":
            duration = input("Please enter the new duration : ").strip()
            if not duration:
                print("No Change.")
            else:
                duration = int(duration)
                if duration < 0:
                    print("Duration can't be negative!")
                else:
                    target_travel["duration"] = duration
                    print("Duration updated.")
                
        elif option == "5":
            booked = target_travel["capacity"] - target_travel["available_seats"]
            capacity = input("Please enter the new capacity : ").strip()
            if not capacity:
                print("No change.")
            else:
                capacity = int(capacity)
                if capacity < booked:
                    print(f"Cannot set capacity below already booked seats ({booked}).")
                else:
                    target_travel["capacity"] = capacity
                    target_travel["available_seats"] = capacity - booked
                    print("Capacity updated successfully.")

        elif option == "6":
            print("You can't change this.")

        elif option == "7":
            price = input("Please enter the new price : ").strip()
            if not price:
                print("No Change.")
            else:
                price = float(price)
                if price < 0:
                    print("Price can't be negative.")
                else:
                    target_travel["price"] = price
                    print("Price updated.")

        elif option == "8":
            status = input("Please enter the new status (active / cancelled / completed) : ").strip().lower()
            if status in ("active", "cancelled", "completed"):
                target_travel["status"] = status
            else:
                print("Invalid status. No change.")

        elif option == "9":
            save_data(TRAVELS_FILE, travels)
            print("Changes saved.")
            return

        else:
            print("Invalid Choice!")

def cancel_travel():

    travels = load_data(TRAVELS_FILE)
    tickets = load_data(TICKETS_FILE)

    travel_id = input("Please enter the travel_id you want to cancel : ")
    
    target_travel = None
    for travel in travels:
        if travel_id == travel["id"]:
            target_travel = travel
            break

    if not target_travel:
        print("Your target travel couldn't be found.")
        # Getting again?
        return
    
    if travel["status"] == "cancelled":
        print("This travel is already cancelled.")
        return
    
    if travel["status"] == "completed":
        print("Cannot cancel a completed travel.")
        return

    confirm = input(f"Are you sure to cancel travel {travel['id']} ({travel['origin']} -> {travel['destination']} at {travel['departure_time']})? (y/n): ").strip().lower()
    if confirm != "y":
        print("Operation got cancelled.")
        return

    travel["status"] = "cancelled"
    travel["available_seats"] = travel["capacity"]

    affected_tickets = 0
    for ticket in tickets:
        if ticket["travel_id"] == travel_id and ticket["status"] in ("reserved", "paid"):
            ticket["status"] = "cancelled"
            affected_tickets += 1

    save_data(TRAVELS_FILE, travels)
    save_data(TICKETS_FILE, tickets)

    print(f"Travel {travel_id} cancelled.")
    print(f"Cancelled tickets: {affected_tickets}")

if __name__ == "__main__":
    print("1. Sign up")
    print("2. Login")
    choice = input("Choose: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
