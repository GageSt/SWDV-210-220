#!/usr/bin/env python3

import csv

FILENAME = "trips.csv"


def get_miles_driven():
# --Successful attempt to add user input into a list thats returned, hindered by personal mishandling of a for x in loop
#
    """   
    miles_driven = []
    while (milesDriven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")  
    miles_driven.append(milesDriven)  
    return miles_driven
    """
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()
    
    tripsList = []
    more = "y"
    """ 
    iteration = 0
    
    while more.lower() == "y":
        iteration += 1
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
        mpg = []

        for x in range(iteration):
            print(f"{x}")
            mpg.append(round(miles_driven[int(x)] // gallons_used[int(x)], 2))
            print(f"Miles Per Gallon:\t{mpg[x]}")
            print()
    """
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round(miles_driven / gallons_used, 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trip = [miles_driven, gallons_used, mpg]
        tripsList.append(trip)
        
        more = input("More entries? (y or n): ")
    
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(tripsList)

    print("Bye!")

if __name__ == "__main__":
    main()

