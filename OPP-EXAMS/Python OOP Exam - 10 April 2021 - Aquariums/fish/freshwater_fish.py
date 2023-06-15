from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    # The FreshwaterFish could only live in FreshwaterAquarium!
    INITIAL_SIZE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.INITIAL_SIZE, price)
        self.name = name
        self.size = self.INITIAL_SIZE
        self.price = price

    def eat(self):
        self.size += 3
