#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    counter = 0
    score = []
    while True:
        user_input = input("Enter test score: ")
        if user_input == "x":
            return score
        else:
            # Unknown problem and fix:
            #validating number as alnum and verifying value range cannot be done in one if statement
            #validating alnum first in a try catch fixes this problem
            try:
                user_input.isalnum() == True
                if int(user_input) >= 0 and int(user_input) <= 100:
                    score.insert(counter, int(user_input))
                    counter += 1 
                else:
                    print("Test score must be from 0 through 100. " +
                        "Score discarded. Try again.")
            except: print("Test score must be a number!. " +
                        "Score discarded. Try again.")

def process_scores(score):
       
    # format and display the result
    print()
    print("Total:             ", sum(score))
    print("Number of Scores:  ", len(score))
    print("Average Score:     ", round(sum(score) / len(score), 2))
    print("Low Score:         ", min(score))
    print("High Score:        ", max(score))
    # The mean is the sorted score's score list item at the length of score divided to an integer by 2
    print("Median Score:      ", sorted(score)[len(score)//2])

def main():
    display_welcome()
    score = get_scores()
    process_scores(score)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


