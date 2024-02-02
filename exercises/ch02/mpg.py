#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gallons_cost = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)

# calculates Total gas cost
cost = gallons_used * gallons_cost
cost = round(cost, 2)

# Calculates cost per mile
cost_per_mile = cost / miles_driven
cost_per_mile = round(cost_per_mile, 2)

# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total Gas Cost:\t\t\t{cost}")
print(f"Cost Per Mile:\t\t\t{cost_per_mile}")
print()
print("Bye!")


