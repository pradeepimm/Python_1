trains = [
    {"no": 101, "name": "Chennai Express", "seats": 5},
    {"no": 102, "name": "Coimbatore Mail", "seats": 3},
    {"no": 103, "name": "Madurai Superfast", "seats": 4}
]

bookings = []

def show_trains():
    print("\nAvailable Trains:")
    print("-" * 40)
    for train in trains:
        print(f"Train No: {train['no']}")
        print(f"Name    : {train['name']}")
        print(f"Seats   : {train['seats']}")
        print("-" * 40)

def book_ticket():
    show_trains()

    train_no = int(input("Enter Train Number: "))
    name = input("Enter Passenger Name: ")

    for train in trains:
        if train["no"] == train_no:
            if train["seats"] > 0:
                train["seats"] -= 1
                bookings.append({
                    "passenger": name,
                    "train_no": train_no,
                    "train_name": train["name"]
                })

                print("\nTicket Booked Successfully!")
                print("Passenger:", name)
                print("Train    :", train["name"])
            else:
                print("Sorry! No seats available.")
            return

    print("Invalid Train Number!")

def view_bookings():
    print("\nBooked Tickets:")
    if len(bookings) == 0:
        print("No bookings yet.")
    else:
        for i, b in enumerate(bookings, start=1):
            print(f"{i}. {b['passenger']} - {b['train_name']} ({b['train_no']})")

# Main Menu
while True:
    print("\n====== Railway Booking System ======")
    print("1. Show Trains")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_trains()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_bookings()
    elif choice == "4":
        print("Thank you for using Railway Booking System.")
        break
    else:
        print("Invalid choice! Try again.")