class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []  # will contain all kids in that room (objects)!
        self.expenses = self.calculate_expenses()

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        total_expenses = 0
        for el in args:
            for sub_el in el:
                if type(sub_el).__name__ != 'Child':
                    total_expenses += sub_el.get_monthly_expense()
                else:
                    total_expenses += sub_el.cost * 30

        return total_expenses

    @staticmethod
    def child_cost(children):
        total_cost = 0
        for child in children:
            total_cost += child.cost
        return total_cost
