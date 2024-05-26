class Inventory:
  def __init__(self):
      '''This function makes a working backpack list'''
      self.backpack = {}
      self.inventory_file = 'inv.txt'

  def pickup(self, item):
      '''This function puts items into the backpack list'''
      self.backpack[item] = True
      self.export()

  def view(self):
      '''This function prints the inventory'''
      print("Inventory:")
      for item in self.backpack:
          print("-", item)

  def export(self):
      '''This function creates an inventory'''
      try:
          with open(self.inventory_file, 'w') as f:
              for item in self.backpack:
                  f.write(item + '\n')
      except:
          print("Something went wrong\n")

  def read(self):
      '''This function prints out the inventory'''
      try:
          with open(self.inventory_file, 'r') as f:
              for line in f:
                  item = line.strip()
                  self.backpack[item] = True
      except:
          print("Something went wrong\n")
