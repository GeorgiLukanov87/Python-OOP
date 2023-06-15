class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []  # all the drivers (objects) participating in the race

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be an empty string!")
        self.__name = value
