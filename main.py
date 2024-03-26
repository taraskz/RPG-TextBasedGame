##############################################################################
# Title: Saving the Kingdom Text Game
# Class: CS 30
# Date: March 13, 2024
# Coders: Taras K
# Version: 002.1
##############################################################################
'''This program is a text based game where the user gets to be a hero and move
   around a castle in order to eventually kill the evil king and save everyone
   from his control
   '''
##############################################################################
#---imports and global variables----------------------------------------------
from tabulate import tabulate

backpack = {}

rooms = {
    "Main Hall": "In front of you is a long hall with expensive paintings and\
 a long red carpet.",
    "Kitchen": "Now you're in the kitchen of the castle, it smells great",
    "Kings Room": "You are in the kings room where he sleeps, hes not here",
    "Dinning Room":"Now you're in the dinning room where the king eats",
    "Throne Room":"You ended up in the throne room where the king sits",
    "Bathroom": "You are in the bathroom where the king does his buisness",
    "Weapon Storage": "You are in the weapon storage room"
        }

room_location = {
    "Main Hall": (0,0), # start
    "Kitchen": (0,-1), # one down
    "Kings Room": (1,-1), # one down 1 right
    "Dinning Room": (0,-2), # two down
    "Throne Room": (1,0), # one right
    "Bathroom": (2,0), # two right
    "Weapon Storage": ()
}

current_location = "Main Hall" #staring position is main hall

directions = {
    "north": (0,1), # up
    "south": (0,-1), # down
    "east": (1,0), # right
    "west": (-1,0) # left
}

# converting rooms into tiles to use in external file 
tile = ["Main Hall", "Kitchen",
  "Kings Room","Dinning Room",
  "Throne Room","Bathroom",
  "Hallway","Weapon Storage"
 ]

# tile location on the map
tiles = [
   [tile[0],tile[5],tile[2]],
   [tile[1],tile[6],tile[4]],
   [tile[6],tile[3],tile[7]]
   ]

# external file name 
mapfile = 'map.txt'

#---functions-----------------------------------------------------------------
def show_room_location():
    print(rooms[current_location]) # prints the location of the player


def movement(direction):
    global current_location
    new_x = room_location[current_location][0] + directions[direction][0] 
    new_y = room_location[current_location][1] + directions[direction][1] 
    new_location = (new_x, new_y)
    # conditional branching 
    if new_location in room_location.values():
        current_location = next(room for room, index in room_location.items() 
                                if index == new_location)
    else:
        print("You hit your head against the wall, try a different direction")


def intro():
    global backpack
    print("You wake up in an unfamiliar place, with a strange woman beside \
you\n")
    print("You've finally woken up hero - she said")
    print("Where am I? - you reply")
    print("The details are not important right now - she said\n")
    print("You are the only person in this kingdom capable of defeating \
the evil king that reigns this kingdom. I need you to take this sword \
and put an end to his evil deeds.\n")
    print("Type 'quit' to exit the game")
    choice = input("Will you take the sword? Yes or no: ")
    # conditional branching
    if choice == "yes":
        backpack["weapons"] = "magical sword"
        print("Great now close your eyes - the witch says\n")
        print("***You close your eyes***")
        print("***You wake up***")
      

def menu():
    while True:
        show_room_location()
        print("Type 'quit' to exit the game")
        print("Here are your movement options:")
        # conditional branching
        for direction in directions:
            print(f"- {direction}")
        direction = input("Choose: ").lower()
        if direction in directions:
            movement(direction)
        if direction == 'quit':
            print("Thanks for playing")
            return False
        if direction not in directions:
          print("Please type the direction correctly")

# creates map in an external file
def export_map():
  try:
      with open(mapfile, 'w') as file:
          file.write(tabulate(tiles, tablefmt = "fancy_grid"))
  except: 
      print("Somethinf went wrong")
  else: 
      print("Here is the map to the castle")
  finally:
      print("Good luck!")


def game():
    intro()
    export_map()
    menu()
#---main----------------------------------------------------------------------
game()
