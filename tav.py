import random
class Tav:
# ask yourself what the bare minimum traits this object must have in order to be part of the class. In this case, the character must have a name and role
# first implement the init function. The init function allows you to create an instance from a class
# self allows you to access instace data from a class

    def __init__(self, name: str, weapon: str):
        # The following line says that this class has a property called name that is equal to whatever name the user input in the beginning
        self.name = name
        self.weapon = weapon

        self.level = 1

        self.ATK = 0
        self.MAXHP = 0
        self.CurrentHP = 0
        self.DEF = 0
        self.Energy = 0
        self.MAXEnergy = 0
        
        self.assign_stats()

    def print_character_sheet(self):
        print('Name: ' + self.name)
        print('Weapon: ' + self.weapon)
        print("Level " + str(self.level))
        print('---------------------------')
        print('ATK: ' + str(self.ATK))
        print('Max HP: ' + str(self.MAXHP))
        print('Current HP: ' + str(self.CurrentHP))
        print('DEF: ' + str(self.DEF))
        print('Energy : '+ str(self.Energy))
        print('Max Energy: ' + str(self.MAXEnergy))





    def assign_stats(self):
        stats = [30, 25, 35, 22]
        random.shuffle(stats)
        self.ATK = stats[0]
        self.MAXHP = stats[1]
        self.DEF = stats[2]
        self.MAXEnergy = stats[3]
        self.CurrentHP = self.MAXHP



