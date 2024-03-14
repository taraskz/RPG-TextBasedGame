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
backpack = {}
def intro():
    print("You wake up in an unfamiliar place, with a strage woman beside \
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
        