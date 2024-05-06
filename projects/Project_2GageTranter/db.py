#!/usr/bin/env/python3
import sqlite3 # Imports the Sql Library
from contextlib import closing
from objects import Player, Position # * works but with unsightly underlines

conn = None # Creates/holds the connection to the database

def connect():
  global conn # Represents the connection variable aboce
  if not conn:  # if Statement to check for the database
    DB_FILE = "Playerdb.db" 
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row # Returns a dictionary for each row in the database rather than a tuple

# Closes The File
def close():
    if conn:
        conn.close()

def get_player_catalog():
  cursor = conn.cursor() # Adds cursor to database which holds the query
  result = cursor.execute('SELECT * FROM Player ORDER BY batOrder') 
  rows = result.fetchall()
  player_catalog = []
  for row in rows:
     fullName = f"{row['firstName']} {row['lastName']}"
     avg = round(row['hits'] / row['atBats'],3)
     player_catalog.append(Player(fullName, row['position'], str(row['atBats']), str(row['hits']), avg))
  #conn.close()
  return player_catalog

def get_position_catalog():
  cursor = conn.cursor() # Adds cursor to database which holds the query
  result = cursor.execute('SELECT * FROM Position ORDER BY PositionID') 
  rows = result.fetchall()
  position_catalog = []
  for row in rows:
     position_catalog.append(Position(row['Position']))
  #conn.close()
  return position_catalog

   
# _____ [ Exception Handling ] _______________________________________________________
# [Lineup Validator]
def get_lineup(prompt, limit): # limit is passed in as the length of player catalog
  while True:
    try:
      number = int(input(prompt))
      if number < 0 or number > limit:
        print("Invalid player number.")
      else:
        return number
    except IndexError:
      print("Invalid whole number. Please try again.\n")
    except ValueError:
      print("Invalid whole number. Please try again.\n")    
# [Integer Validator]
def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Invalid whole number. Please try again.\n")

# [Positions Object Validator]
def get_pos(prompt, position_catalog): 
  while True:
    #print(f"{position_catalog[0]}")
    position = input(prompt)
    print(f"You Entered: {position}")
    for i, Position in enumerate(position_catalog):
       
       entry1 = str(position)
       entry2 = str(Position.getPos())
       #print(f"{entry1} + {entry2} To Be Compared")
       #print(f"Pos Test: {Position.getPos()}")
       #print(f"Does {position} equal {Position.getPos()}")
       if  entry1 == entry2:
          return position
       #else:
          #print(f"{Position.getPos()}: Failed")
    else:
       print("Invalid position. Try again")


# "2" [Add New Player]
def add_player(player_catalog, position_catalog):
  name = input("Name: ")
  try:
    fullname = name.split(None, 1)
    firstName = fullname[0]
    lastName = fullname[1]
  except IndexError:
     print("Did you forget the last name???")
     return
  position = get_pos("Position: ", position_catalog)
  bats = str(get_int("At Bats: "))
  hits = str(get_int("Hits: "))
  avg = str(round(int(hits)/int(bats), 3))
  batOrder = len(player_catalog) + 1
  player = Player(name,
            position,
            bats,
            hits,
            avg)
  print(player)
  with closing(conn.cursor()) as c:
     sql = '''INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits)
      VALUES (?, ?, ?, ?, ?, ?)'''
     c.execute(sql, (batOrder, firstName, lastName, position, bats, hits))
     conn.commit()

  player_catalog.append(player)
  print(player.name + " was added.\n")

# "3" [Remove Existing Player]
def remove_player(player_catalog):
  number = get_int("Number: ")
  sql = 'SELECT * FROM Player WHERE batOrder = ?'
  cursor = conn.cursor() # Adds cursor to database which holds the query
  result = cursor.execute(sql, (number,)) 
  rows = result.fetchall()#Pick a player from the list    
  row = rows[0]
  fullName = f"{row['firstName']} {row['lastName']}"
  print(fullName + " was selected.")               #Show name of selected player
  if number < 1 or number > len(player_catalog):
      print("Invalid player number.\n")
  else:
        delete_player(number)
        print(f"{fullName} was removed from the db")

def delete_player(number):
    sql = 'DELETE FROM Player WHERE playerID = ?'
    cur = conn.cursor()
    cur.execute(sql, (number,))
    conn.commit()

     

# "4" [Move Player List Position]
def move_player(player_catalog):
  number = get_lineup("Current Lineup Number: ", len(player_catalog))
  sql = 'SELECT * FROM Player WHERE batOrder = ?'
  cursor = conn.cursor() # Adds cursor to database which holds the query
  result = cursor.execute(sql, (number,)) 
  rows = result.fetchall()#Pick a player from the list    
  row = rows[0]
  fullName = f"{row['firstName']} {row['lastName']}"
  print(fullName + " was selected.")               #Show name of selected player
  new_number = get_lineup("New lineup number: ", len(player_catalog))       #Get new list position
  playerVar = row['playerID']

  sql = 'UPDATE Player SET batOrder = ? WHERE batOrder = ?'
  cursor = conn.cursor()
  cursor.execute(sql, (number, new_number))
  conn.commit
  #Update player who has new number to have old number of previously updated player

  sql = 'UPDATE Player SET batOrder = ? WHERE playerID = ?'
  cursor = conn.cursor()
  cursor.execute(sql, (new_number, playerVar))
  conn.commit()
  print(fullName + " was moved.\n")

# "5" [Edit Player Field Position]     
def edit_position(player_catalog, position_catalog):
   number = get_lineup("Lineup Number: ", len(player_catalog))
   sql = 'SELECT * FROM Player WHERE batOrder = ?'
   cursor = conn.cursor() # Adds cursor to database which holds the query
   result = cursor.execute(sql, (number,)) 
   rows = result.fetchall()#Pick a player from the list    
   row = rows[0]
   fullName = f"{row['firstName']} {row['lastName']}"
   print(fullName + " was selected.")
   print("Position = " + row['position'])
   new_position = get_pos("New Position: ", position_catalog)
   sql = 'UPDATE Player SET position = ? WHERE batOrder = ?'
   cursor = conn.cursor()
   cursor.execute(sql, (new_position, number))
   conn.commit()
   print(f"{fullName} was updated.\n")

# "6" [Edit Player Stats]
def edit_stats(player_catalog):
   number = get_lineup("Select Player: ", len(player_catalog))
   sql = 'SELECT * FROM Player WHERE batOrder = ?'
   cursor = conn.cursor() # Adds cursor to database which holds the query
   result = cursor.execute(sql, (number,)) 
   rows = result.fetchall()#Pick a player from the list    
   row = rows[0]
   avg = round(row['hits'] / row['atBats'],3)
   fullName = f"{row['firstName']} {row['lastName']}"
   print(f"You selected: {fullName} AB={row['atBats']} H={row['hits']} AVG={avg}")
   new_bats = get_int("At bats: ")
   new_hits = get_int("Hits: ")
   sql = 'UPDATE Player SET atBats = ?, hits = ? WHERE batOrder = ?'
   cursor = conn.cursor()
   cursor.execute(sql, (new_bats, new_hits, number))
   conn.commit()
   print(f"{fullName}  was updated.\n")