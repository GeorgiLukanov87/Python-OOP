from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.family_name = family_name
        self.budget = pension_one + pension_two
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
        self.room_cost = 15
        self.expenses = self.calculate_expenses(self.appliances)
