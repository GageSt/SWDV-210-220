#!/usr/bin/env python3
from validation import get_float, get_int
def calculate_future_value(monthly_investment, yearly_interest, years:int) -> float:
    # convert yearly values to monthly values
    years
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value



def main():
    import random
    random.randint
    choice = "y"
    while choice.lower() == "y":
        
        # get input from the user
        monthly_investment = get_float("Enter monthly investment: ", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate:", 0, 15)
        years = get_int("Enter number of years:      ", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()
        
        """
        get_float('Testing float:', -10.0, -5.0)
        get_int('Testing int:', 5, 10)
        """

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()




