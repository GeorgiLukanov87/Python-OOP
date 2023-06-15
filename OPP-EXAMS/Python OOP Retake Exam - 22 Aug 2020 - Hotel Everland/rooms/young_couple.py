from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.family_name = family_name
        self.budget = salary_one + salary_two
        self.members_count = 2
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.room_cost = 20
        self.expenses = self.calculate_expenses(self.appliances)
