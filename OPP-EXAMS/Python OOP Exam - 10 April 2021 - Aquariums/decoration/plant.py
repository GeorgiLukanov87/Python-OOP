from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    COMFORT = 5
    PRICE = 10

    def __init__(self):
        super().__init__(self.COMFORT, self.PRICE)
        self.comfort = self.COMFORT
        self.price = self.PRICE
