#!/usr/bin/env python3
        
# def calculate_future_value(monthly_investment, yearly_interest, years):
#     # convert yearly values to monthly values
#     monthly_interest_rate = yearly_interest / 12 / 100
#     months = years * 12

#     # calculate future value
#     future_value = 0.0
#     for i in range(months):
#         future_value += monthly_investment
#         monthly_interest = future_value * monthly_interest_rate
#         future_value += monthly_interest

#     return future_value

def get_float(prompt, lower, upper):
    float_input = input(f'{prompt}\t')
    try:
      valid_float = float(float_input)
      # print(f'valid float: {valid_float}')
      in_bounds = (valid_float > lower) and (valid_float <= upper)
      if in_bounds:
          return valid_float
      else:
        print(f"Please enter number larger than {lower} and smaller than or equal to {upper}!")
        return get_float(prompt, lower, upper)
    except ValueError:
        print("Please enter a valid float!")
        return get_float(prompt, lower, upper)

# old, cannot parse negative numbers
# def get_int(prompt, lower, upper):
#     int_input = input(f'{prompt}\t')
#     if int_input.isdigit() == False:
#         print("Please enter a valid number!")
#         return get_int(prompt, lower, upper)
#     elif int(int_input) < lower or int(int_input) > upper:
#         print(f"Entry must be greater than {lower} and less than or equal to {upper}")
#         return get_int(prompt, lower, upper)
#     else:
#         valid_int = int(int_input)
#         return valid_int

def get_int(prompt, lower, upper):
    int_input = input(f'{prompt}\t')
    try:
        valid_int = int(int_input)
        in_bounds = valid_int > lower and valid_int < upper
        if in_bounds:
          return valid_int
        else:
          print(f"Entry must be greater than {lower} and less than or equal to {upper}")
          return get_int(prompt, lower, upper)
    except ValueError:
        print("Please enter a valid int!")
        


def main():
    
    choice = "y"
    while choice.lower() == "y":
        
        get_float('Testing float:', -10.0, -5.0)
        get_int('Testing int:', 5, 10)

        # # get input from the user
        # monthly_investment = get_float("Please enter your monthly investment", 0, 1000)
        # yearly_interest_rate = get_float("Please enter your yearly interest rate", 0, 15)
        # years = get_int("Enter number of years", 0, 50)

        # # get and display future value
        # future_value = calculate_future_value(
        #     monthly_investment, yearly_interest_rate, years)

        # print(f"Future value:\t\t\t{round(future_value, 2)}")
        # print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()




