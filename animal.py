class Animal:
    def __init__(self, name: str, species: str, warm_blooded: bool):
        self.name = name
        self.species = species
        
    def eat(self, food: str):
        print(self.name + ' the ' + self.species + ' eats ' + food + '.') 