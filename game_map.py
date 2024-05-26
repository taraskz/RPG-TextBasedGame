from tabulate import tabulate


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
        print("Something went wrong\n")


# print out the map to the console for the user to see
def read_map():
    '''This function prints the map'''
    # conditional branching 
    try:
        with open(mapfile, 'r') as file:
          print(file.read())
    except:
        print("Something went wrong\n")
