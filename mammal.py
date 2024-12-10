from animal import Animal

class Mammal(Animal):
    def __init__(self, name: str, species: str, hair_color: str, warm_blooded: bool):
        super().__init__()
        self.warm_blooded == True
        self.hair_color = hair_color

    def sleep(self):
        print(self.name + ' the ' + self.hair_color + ' colored ' + self.species + " falls a sleep...")
        print(super().eat("cookies"))

