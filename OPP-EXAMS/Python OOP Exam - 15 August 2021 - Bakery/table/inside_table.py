from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not 1 <= value <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value

    def reserve(self, number_of_people):
        if self.capacity >= number_of_people and not self.is_reserved:
            self.number_of_people += number_of_people
            self.is_reserved = True
            return f'Table {self.table_number} has been reserved for {number_of_people} people'
        else:
            return f'No available table for {number_of_people} people'

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum([d.price for d in self.drink_orders]) + sum([f.price for f in self.food_orders])

    def clear(self):
        self.drink_orders = []
        self.food_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}" + \
                   f'\nType: {self.__class__.__name__}' \
                   + f"\nCapacity: {self.capacity}"
