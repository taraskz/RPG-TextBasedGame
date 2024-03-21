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
    "Main Hall": (0,0), # start
    "Kitchen": (0,-1), # one down
    "Kings Room": (1,-1), # one down 1 right
    "Dinning Room": (0,-2), # two down
    "Throne Room": (1,0), # one right
    "Bathroom": (2,0) # two right
}

current_location = "Main Hall" #staring position is main hall

directions = {
    "north": (0,1), # up
    "south": (0,-1), # down
    "east": (1,0), # right
    "west": (-1,0) # left
}
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
    else:
      if choice == "quit":
        print("Thanks for playing")
        return intro()
      

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
          

def game():
    intro()
    menu()
#---main----------------------------------------------------------------------
game()
