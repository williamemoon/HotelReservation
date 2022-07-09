#William Moon CIS 261 Week 1 Lab 3 Hotel Reservation

from datetime import datetime

print("Welcome to the Hotel Reservation Program\n")

#next_reservation loop
next_reservation = "y"
while next_reservation.lower() == "y":
    #checkin date
    while True:
        date_str = input("Enter your checkin Date (YYYY-MM-DD): ")
        try:
            checkin_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("I'm sorry I didn't understand.  Please enter a date YYYY-MM-DD")
            print(" ")
            continue 

        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if today > checkin_date:
            print("We are out of rooms currently, please schedule a time in the future.")
            print()
        else: 
            break

    #checkout date
    while True:
        date_str = input("When would you like to checkout? (YYYY-MM-DD): ")
        try:
            checkout_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("I'm sorry I didn't understand that.  Please enter a date YYYY-MM-DD")
            print(" ")
            continue

        if checkout_date <= checkin_date:
            print("You must check in before checking out.  Please enter a date after your checin date.  ")
            print (" ")
        else:
            break

    #math 
    rate = 85.00
    rate_memo = ""
    if checkin_date.month == 8:
        rate = 105.00
        rate_memo = "(Travel Season)"
    total_nights = (checkout_date - checkin_date).days
    total_cost = rate * total_nights

    #output
    date_format = "%B %d, %Y"
    print(f"Checkin Date:     {checkin_date:{date_format}}")
    print(f"Checkout Date:    {checkout_date:{date_format}}")
    print(f"Nightly Rate:     {rate} {rate_memo}")
    print(f"Total Nights:     {total_nights}")
    print(f"Total Price:      {total_cost}")
    print(" ")

next_reservation = input("Would you like to make another reservation?  (y/n):  ")
print(" ")


  


