class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.cost = sum(x for x in toys_cost) + self.food_cost

