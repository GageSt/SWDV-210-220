#!/usr/bin/env python3

from datetime import date, datetime, timedelta

def get_invoice_date():
    while True:
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")  
        try:                                                      # Begin Exception Handling
            date_time = datetime.strptime(invoice_date_str, "%m/%d/%Y")  # Try to turn user input (invoice_date_str) into a MM/DD/YYYY datetime object named date_time
        except ValueError:
            print(f"Invalid date format! Try again.")
            continue  # keyword that ends the loop iteration

        invoice_date = date(date_time.year, date_time.month, date_time.day) #create a date object from the datetime object

        if invoice_date > date.today(): #Creates a date object set by the today function to compare with the invoice_date object
            print("Invoice date must be today or earlier. Try again.")
        else: 
            return invoice_date

def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today() #Changed from datetime.now() which set the current_date variable to a datetime value set by the now() function
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
