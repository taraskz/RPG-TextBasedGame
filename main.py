##############################################################################
# Title: Saving the Kingdom Text Game
# Class: CS 30
# Date: March 13, 2024
# Coders: Taras K
# Version: 004
##############################################################################
'''This program is a text based game where the user gets to be a hero and move
   around a castle in order to eventually kill the evil king and save everyone
   from his control
   '''
##############################################################################
#---imports and global variables----------------------------------------------
from inventory import Inventory
from tabulate import tabulate
from player import Player
from enemy import EvilKing

inventory = Inventory()
player = Player(name="Hero")
evil_king = EvilKing()

chests = {
    "Main Hall": ["health potion"],
    "Kitchen": ["kitchen knife", "apple"],
    "Kings Room": ["ancient royal sword"]
          }


rooms = {
    "Main Hall": "You ate in the main hall, in front of you is a long hall with \
expensive paintings and a long red carpet.",
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
    '''This function prints the current location of the player after each move
    '''
    print(rooms[current_location]) 


def movement(direction):
    '''This function handles the movement input of the player'''
    global current_location
    new_x = room_location[current_location][0] + directions[direction][0] 
    new_y = room_location[current_location][1] + directions[direction][1] 
    new_location = (new_x, new_y)
    # conditional branching 
    if new_location in room_location.values():
        current_location = next(room for room, index in room_location.items()
                                if index == new_location)
        if current_location == "Throne Room":
            encounter_evil_king()
    else:
        print("You hit your head against the wall try a different direction")

# the intro to the game
def intro():
    '''This function prints all the info for the introduction of the game'''
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
        inventory.pickup("magical sword")
        inventory.export()
        player.add_ability("swordsmanship")
        print("Great now close your eyes - the witch says\n")
        print("***You close your eyes***")
        print("***You wake up in an unfamiliar castle***")
    else:
        print("You refused the sword. Next time accept it, the game \
will now end")
        exit_game()


def check_for_chest():
  # sub menu for checking if there is a chest in area and pick up items
    if current_location in chests:
        inside_chest = chests[current_location]
        if inside_chest:
            print("You found a chest")
            for item in inside_chest:
                print(f"- {item}")
            pickup_item = input("Do you want to loot the chest? Yes or no: ")
            if pickup_item.lower() == "yes":
                for item in inside_chest:
                    inventory.pickup(item)
                # removing items from the chest
                chests[current_location].clear()
                print("The item is in your inventory")
            else:
                print("You left the chest alone")
        else:
            print("You left the chest alone")


def encounter_evil_king():
    '''This function creates a fight with the evil king when the player 
        encounters him
        '''
    print(f"You entered {current_location}. the Evil King whats to fight you")
    while player.is_alive() and evil_king.is_alive():
        action = input("Do you want to 'attack' or 'run':\n").lower()
        if action == 'attack':
            damage = 50
            evil_king.take_damage(damage)
            print(f"You attacked the Evil King and dealt {damage} damage")
            if evil_king.is_alive():
                print(f"The Evil King has {evil_king.health} remaining health\n")
                player_damage = 20
                player.take_damage(player_damage)
                print(f"The Evil King attacked back and dealt {player_damage} \
damage")
                print(f"You have {player.health} health remaining\n")
            else:
                print("Congrts you have defeated the Evil King and saved \
the kingdom!!!!")
                exit_game()

        elif action == 'run':
            print("You ran away!!")
            movement("south")
            return
        else:
            print("Invalid action type it property")
            
    if not player.is_alive():
        print("You got defeated by the Evil King... Game over!!!")
        exit()


# main game menu
def menu():
    '''This function is the main menu where the player chooses the action
       they want to perform like walk, look at the map or inventory
       '''
    while True:
        inventory.read()
        show_room_location() # prints current location
        check_for_chest() # checks if there is chest in a room
        print("Type 'quit' to exit the game\n")
        print("Type 'inventory' to see your inventory\n")
        print("Type 'abilities' to see your abilities\n")
        print("Type 'map' to view map\n")
        print("Here are your movement options:\n")
        # conditional branching
        for direction in directions:
            print(f"- {direction}")
        direction = input("Choose: ").lower()
        if direction in directions:
            movement(direction)
        elif direction == 'inventory':
            inventory.view()
        elif direction == 'abilities':
            player.view_abilities()
        elif direction == 'map':
            read_map()
        elif direction == 'quit':
            print("Thanks for playing")
            return False
        elif direction not in directions:
          print("Please type the direction/action correctly")


# creates map in an external file
def export_map():
    '''This function creates the map of the game so that the player can view
       it later
       '''
    # conditional branching
    try:
        with open(mapfile, 'w') as file:
            file.write(tabulate(tiles, tablefmt = "double_grid"))
    except:
        print("Something went wrong")
    else:
        print("Here is the map of the castle")
    finally:
        print("Good luck...")


# print out the map to the console for the user to see
def read_map():
    '''This function prints the map'''
    # conditional branching 
    try:
        with open(mapfile, 'r') as file:
          print(file.read())
    except:
        print("Something went wrong")
    else:
        print("Here is the map to the castle")
    finally:
        print("Good luck...")


def exit_game():
    '''This function runs when the evil king is defeated and it ends 
    the game
    '''
    print("Thanks for playing and saving the kingdom. The game is over now")
    exit()


# main game 
def game():
    '''This function acts as a main game'''
    intro()
    menu()
#---main----------------------------------------------------------------------
game()

