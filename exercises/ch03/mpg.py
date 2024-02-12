#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

answer = "y"
while answer.lower() == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost Per Gallon must be greater than zero. Please try again. ")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        total = round(gallons_used * cost_per_gallon, 2)
        cost = round(cost_per_gallon / mpg, 1)

        print()
        print("Miles Per Gallon:        ", mpg)
        print("Total Gas Cost:          ", total)
        print("Cost Per Mile:           ", cost)
        print()
        answer = input("Get entries for another trip (y/n)? ")

print()
print("Bye!")



