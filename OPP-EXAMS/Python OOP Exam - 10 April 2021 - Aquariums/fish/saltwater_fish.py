from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    # The SaltwaterFish could only live in SaltwaterAquarium!
    INITIAL_SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.INITIAL_SIZE, price)
        self.name = name
        self.species = species
        self.size = self.INITIAL_SIZE
        self.price = price

    def eat(self):
        self.size += 2
