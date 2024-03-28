##############################################################################
# Title: Saving the Kingdom Text Game
# Class: CS 30
# Date: March 13, 2024
# Coders: Taras K
# Version: 003
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
    "Weapon Storage": "You are in the weapon storage room",
    "Hallway_1": "You are in a hallway",
    "Hallway_2": "You are in a hallway"
        }

room_location = {
    "Main Hall": (0,0),"Bathroom": (1,0),"Kings Room": (2,0),
    "Kitchen": (0,-1),"Hallway_2": (1,-1),"Throne Room": (2,-1), 
    "Hallway_1": (0,-2),"Dinning Room": (1,-2),"Weapon Storage": (2,-2),
}

current_location = "Main Hall" #staring position is main hall

directions = {
    "north": (0,1), # up
    "south": (0,-1), # down
    "east": (1,0), # right
    "west": (-1,0) # left
}

# converting rooms into tiles to use in external file 
tile = ["Main Hall", "Kitchen","Kings Room","Dinning Room",
  "Throne Room","Bathroom","Weapon Storage", "Hallway_1",
  "Hallway_2"
 ]

# tile location on the map
tiles = [
   [tile[0],tile[5],tile[2]],
   [tile[1],tile[8],tile[4]],
   [tile[7],tile[3],tile[6]]
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

# the intro to the game
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
      
# main game menu
def menu():
    while True:
        read_map()
        show_room_location()
        print("Type 'quit' to exit the game\n")
        print("Type 'inventory' to see your inventory\n")
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

def sub_menu():
    print()
    

def print_backpack():
    global backpack
    print("Here is what's in your backpack")
    print(f"weapons: {backpack['weapons']}")
    
    
  
# creates map in an external file
def export_map():
  # conditional branching
  try:
      with open(mapfile, 'w') as file:
          file.write(tabulate(tiles, tablefmt = "double_grid"))
  except: 
      print("Somethinf went wrong")
  else: 
      print("Here is the map of the castle")
  finally:
      print("Good luck!")


# print out the map to the console for the user to see
def read_map():
    try:
        with open(mapfile, 'r') as file:
          print(file.read())
    except:
        print("Something went wrong")
    else:
        print("Here is the map to the castle")
    finally:
        print("Good luck")


# main game 
def game():
    intro()
    menu()
#---main----------------------------------------------------------------------
export_map()
game()
