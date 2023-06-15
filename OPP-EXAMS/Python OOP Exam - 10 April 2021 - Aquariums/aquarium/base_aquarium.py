from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

        self.decorations = []  # decorations (objects).
        self.fish = []  # all the fish (objects).

    # All passed names would be UNIQUE !!!
    # and it will not be necessary to check if a given name already exists.
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @abstractmethod
    def calculate_comfort(self):
        ...

    @abstractmethod
    def add_fish(self, fish):  # add Fish OBJECT!
        ...

    @abstractmethod
    def remove_fish(self, fish):  # remove Fish OBJECT!
        ...

    @abstractmethod
    def add_decoration(self, decoration):  # remove Decoration OBJECT!
        ...

    @abstractmethod
    def feed(self):  # feed all fish in the aquarium
        ...

    def __str__(self):
        ...
