def main():
    full_name = get_full_name()
    print()
    
    password = get_password()
    print()

    email = get_email()
    print()

    phone = get_phone()
    
    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.\nWe'll text your confirmation code to this number:    {phone}")             
    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password

def get_email():
    while True:
        at_symbol = False
        period = False
        email = input("Enter email address:         ").strip()
        for char in email:
            if char.find("@"):
                at_symbol = True
            elif char.find("."):
                period = True
        if at_symbol == False or period == False:
            print(f"Please enter a valid email address")
        else:
            return email

def get_phone():
    while True:
        phone = input("Enter phone number:          ").strip()
        phone = phone.replace("-","")
        phone = phone.replace(".","")
        phone = phone.replace(" ","")
        for char in phone:
            if len(phone) != 10:
                print(f"Please enter a 10-digit phone number")
            else:
                # Adds first 3 digits, a period, the 3rd to 6th digits, a period, and the remaining string past digit 6
                phone = phone[0:3] + "." + phone[3:6] + "." + phone[6:]
                return phone
        
if __name__ == "__main__":
    main()
