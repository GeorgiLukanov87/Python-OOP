from project.appliances.appliance import Appliance


class Fridge(Appliance):
    COST = 1.2

    def __init__(self):
        super().__init__(self.COST)
        self.cost = self.COST

    def get_monthly_expense(self):
        return self.cost * 30

    def calculate_cost(self, toys_cost):
        total_cost = 0
        for cost in toys_cost:
            total_cost += cost
        return total_cost + self.get_monthly_expense()
