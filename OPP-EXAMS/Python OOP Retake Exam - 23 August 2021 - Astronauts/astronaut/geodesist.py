from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_UNITS_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_UNITS_OXYGEN)

    def breathe(self):
        self.oxygen -= 10
