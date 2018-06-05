FLIGHTS = {"Barcelona": 120, "Madrid": 145, "Venice": 175, "Berlin": 110,
    "Dublin": 80, "Amsterdam": 85, "Paris": 105, "Athens": 220,
    "Ibiza": 230, "New York": 550, "Sydney": 825, "Tokyo": 675}

def print_help():
    print("""\nTo use this program you must choose a flight.\nYou can either type o to select a flight,\nor q to exit the application.\n""")

title = print("""=================
=Worpel Airlines=
=================""")

print_help()

for flight in FLIGHTS:
    print("£" + str(FLIGHTS[flight]) + "|\t" + flight)

def get_details():
    user_name = input("\nPlease enter your full name: ")
    user_email = input("Please enter your email address: ")
    print("\nYour name is:",user_name)

def flight_choice():
    destination = input("What is your destination? ")
    if destination in FLIGHTS:
        print("You have selected",destination)
        adult_seats = int(input("How many adult seats do you require?: "))
        child_seats = int(input("How many child seats do you require?: "))
        adult_price = adult_seats * FLIGHTS[destination]
        child_price = child_seats * FLIGHTS[destination] * 0.6
        total_cost = adult_price + child_price
        print_total = print("\nThe total cost of your journey is £",total_cost)
        user_continue = input("Would you like to continue?: ")
        if user_continue == "y" or user_continue == "yes":
            get_details()
            print("Your destination is:",destination)
            print("The total cost of your journey is £",total_cost)
            user_confirm = input("\nWould you like to confirm your booking?: ")
            if user_confirm == "y" or "yes":
                print("Your booking details have been sent to your email address")
            else:
                exit()
        else:
            exit()
    else:
        print("Invalid selection")
        flight_choice()

def options():
    choice = input("\nChoose either o, q or h: ")
    if choice.lower() == "o":
        flight_choice()
    elif choice.lower() == "h":
        print_help()
        choice = input("Choose either o, q or h: ")
    elif choice.lower() == "q":
        exit()
    else:
        print("Invalid input. Choose either o, h or q")

options()