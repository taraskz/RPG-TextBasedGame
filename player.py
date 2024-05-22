class Player:
    def __init__(self, name, health = 100):
        '''This function has a player with a name, health, and abilities'''
        self.name = name
        self.health = health
        self.abilities = []

    def add_ability(self, ability):
        '''This function allows a player to get abilities'''
        self.abilities.append(ability)

    def view_abilities(self):
        '''Prints the player's abilities'''
        print("Abilities:")
        for ability in self.abilities:
            print("-", ability)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        '''Checks if player is alive'''
        return self.health > 0
    
