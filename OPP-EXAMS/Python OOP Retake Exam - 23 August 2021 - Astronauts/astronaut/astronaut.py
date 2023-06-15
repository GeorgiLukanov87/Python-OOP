from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    @abstractmethod
    def breathe(self):
        ...

    def __str__(self):
        if not self.backpack:
            self.backpack = ['none']

        return f'Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {", ".join(self.backpack)}\n'
