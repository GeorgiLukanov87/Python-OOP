from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.family_name = family_name
        self.budget = salary
        self.members_count = 1
        self.appliances = [TV()]
        self.room_cost = 10
        self.expenses = self.calculate_expenses(self.appliances)
