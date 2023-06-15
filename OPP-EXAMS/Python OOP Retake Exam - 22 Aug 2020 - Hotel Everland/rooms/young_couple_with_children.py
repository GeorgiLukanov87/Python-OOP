from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_two + salary_one, 2 + len(children))
        self.family_name = family_name
        self.budget = salary_one + salary_two
        self.children = [*children]
        self.members_count = 2 + len(children)
        self.room_cost = 30
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.appliances.extend(self.extra_items(children))
        self.expenses = self.calculate_expenses(self.appliances, children)

    @staticmethod
    def extra_items(children):
        extra_items_need = []
        for _ in children:
            extra_items_need.extend([TV(), Fridge(), Laptop()])
        return [*extra_items_need]
