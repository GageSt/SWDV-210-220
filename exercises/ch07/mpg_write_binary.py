#!/usr/bin/env python3


import pickle, json

FILENAME = "tripsList.bin"


def get_miles_driven():
  
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def read_list():
    with open(FILENAME, "rb") as file:
        trips = pickle.load(file)
#        print(trips)                           
#        print(json.dumps(trips, indent=2))
    return trips
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()
    
    tripsList = []
    more = "y"
    
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round(miles_driven / gallons_used, 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trip = [miles_driven, gallons_used, mpg]
        tripsList.append(trip)
        
        more = input("More entries? (y or n): ")
    
    with open(FILENAME, "wb") as file:
      pickle.dump(tripsList, file)

    print("Bye!")
    tripsList = read_list()

    print(f"Distance\tGallons\t\tMPG")
    for i, trips in enumerate(tripsList, start=1):
        print(f"{i}. {trips[0]}\t{trips[1]}\t\t{trips[2]}")
    

if __name__ == "__main__":
    main()

