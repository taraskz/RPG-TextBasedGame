##############################################################################
# Title: Saving the Kingdom Text Game
# Class: CS 30
# Date: March 13, 2024
# Coders: Taras K
# Version: 002
##############################################################################
'''This program is a text based game where the user gets to be a hero and move
   around a castle in order to eventually kill the evil king and save everyone
   from his control
   '''
##############################################################################
#---imports and global variables----------------------------------------------
backpack = {}

rooms = {
    "Main Hall": "In front of you is a long hall with expensive paintings and\
a long red carpet.",
    "Kitchen": "Now you're in the kitchen of the castle, it smells great",
    "Kings Room": "You are in the kings room where he sleeps, hes not here",
    "Dinning Room":"Now you're in the dinning room where the king eats",
    "Throne Room":"You ended up in the throne room where the king sits"
        }

room_location = {
    "Main Hall": (0,0),
    "Kitchen": (0,-1),
    "Kings Room": (1,-1),
    "Dinning Room": (0,-2),
    "Throne Room": (1,0)
}

current_location = "Main Hall" #staring position

directions = {
    "north": (0,1),
    "south": (0.-1),
    "east": (1,0),
    "west": (-1,0)
}
#---functions-----------------------------------------------------------------
def show_room_location():
    print(rooms[current_location]) # prints the location of the player


def movement(direction):
    global current_location
    new_x = room_location[current_location[0] + directions[0]] # adds x value
    new_y = room_location[current_location[1] + directions[1]] # adds y value
    new_location = (new_x, new_y)
    if new_location in room_location:
        current_location = next(room for room, index in room_location.items() 
                                if index == new_location)
    else:
        print("Unfortunetly you can't go there, try again")


def intro():
    print("You wake up in an unfamiliar place, with a strange woman beside \
you\n")
    print("You've finally woken up hero - she said")
    print("Where am I? - you reply")
    print("The details are not important right now - she said\n")
    print("You are the only person in this kingdom capable of defeating \
the evil king that reigns this kingdom. I need you to take this sword \
and put an end to his evil deeds.")
    choice = input("Will you take the sword? Yes or no: ")
    if choice == "yes":
        backpack["weapons"] = "magical sword"
        print("Great now close your eyes - the witch says\n")
        print("***You close your eyes***")
    

def menu():
    print("***You wake up***")
    show_room_location()
    print("Here are your movement options:")
    for direction in directions:
        print(f"{direction}")
    direction = input("Choose: ").lower()
    if direction in directions:
        move(direction)
    else:
        print("Wrong direction.")
    

#---main----------------------------------------------------------------------
#intro()
menu()