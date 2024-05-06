#!/usr/bin/env/python3
from datetime import date, datetime, timedelta
from objects import *
from db import *

# "0" [Get Date]
def get_date():
  while True:
    today = date.today()
    print(f"Current Date: {today}")
    game_date_str = input("Game date (YYYY/M/D): ") 
    print(f"Entered Date: {game_date_str}")   
    try:
        dt = datetime.strptime(game_date_str,  "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format! Try again.")
        continue
    game_date = date(dt.year, dt.month, dt.day)
    if game_date < date.today():
        print("Invoice date must be today or earlier. Try again.")
    else:
        days_until =  game_date - date.today()
        print(f"{days_until.days}")
        if int(days_until.days) < 0:
           print("You have entered a date earlier than today.")
        print(f"DAYS UNTIL GAME: {days_until.days}")
        return

# "1" [Show List]
def display_list(): 
  player_catalog = get_player_catalog()
  if len(player_catalog) == 0:
    print("There are no players in the list.\n")
    return
  else:
    for i, player in enumerate(player_catalog, start=1):
      print(f"{'Player':24s}{'Pos':6s}{'AB':6s}{'H':6s}{'AVG':5s}")
      print(f"{i}. {player.getStr()}")
      print()

# [Menu Display]
def title():
  titleTxt = "Baseball Team Manager"
  title = titleTxt.center(60, " ")
  print(title)
  print("MENU OPTIONS")
  print("1 - Display lineup")
  print("2 - Add player")
  print("3 - Remove player")
  print("4 - Move player")
  print("5 - Edit player position")
  print("6 - Edit player status")
  print("7 - Exit Program")

def show_positions(position_catalog):
  print("POSITIONS\n") 
  for i, Position in enumerate(position_catalog):
    entry1 = Position.pos
    print(f"{entry1}", end="  ")
  print("\n")

def seperator_line():
  print("==================================================================")

def main():

  player_catalog = [ Player("Tommy La Stella", "3B", "360", "0", 0.274),
                       Player("Mike Yastrzemski", "RF", "563", "169", 0.281),
                       Player("Buster Posey", "C", "4575", "1380", "0.302"),
                       Player( "Brandon Belt", "1B", "3811", "1003", 0.263), 
                       Player("Brandon Crawford", "SS", "4402", "1099", 0.250),
                       Player("Alex Dickerson", "LF", "586", "160", 0.273),
                       Player("Austin Slater", "CF", "569", "147", 0.274),
                       Player("Kevin Gausman", "P", "56", "2", 0.036)]
  
  position_catalog = [ Position("C"),
                       Position("1B"),
                       Position("2B"),
                       Position("3B"),
                       Position("SS"),
                       Position("LF"),
                       Position("CF"),
                       Position("RF"),
                       Position("P")]
  connect()
  title()
  seperator_line()
  get_date()
  seperator_line()
  title()
  show_positions(get_position_catalog())
  seperator_line()

  while True:
    command = input("Menu Option: ")
    if command == "1":
      display_list()
      print()
    elif command == "2":
      add_player(get_player_catalog(), get_position_catalog())
    elif command == "3":
      remove_player(get_player_catalog())
    elif command == "4":
      move_player(get_player_catalog())
    elif command == "5":
      edit_position(get_player_catalog(), get_position_catalog())
    elif command == "6":
      edit_stats(get_player_catalog()) 
    elif command == "7":
      print("Bye!")
      break
    else:
      print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
  main()