from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_UNITS_OXYGEN = 90

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_UNITS_OXYGEN)

    def breathe(self):
        self.oxygen -= 15
