class EvilKing:
    def __init__(self, name = "Evil King", health = 100):
        '''This function creates the evil king enemy'''
        self.name = name
        self.health = health

    def take_damage(self, damage):
        '''Makes the evil king take damage'''
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        '''Checks if the evil king is alive'''
        return self.health > 0