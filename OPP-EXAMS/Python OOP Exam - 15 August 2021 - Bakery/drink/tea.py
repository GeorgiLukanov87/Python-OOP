from project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, 2.50, brand)

    def __str__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
