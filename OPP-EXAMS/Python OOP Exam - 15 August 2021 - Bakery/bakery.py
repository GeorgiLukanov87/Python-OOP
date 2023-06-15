from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        food_mapper = {'Bread': Bread, 'Cake': Cake}
        if food_type in food_mapper.keys():
            if name in [b.name for b in self.food_menu]:
                raise Exception(f"{food_type} {name} is already in the menu!")
            else:
                new_food = food_mapper[food_type](name, price)
                self.food_menu.append(new_food)
                return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        drink_mapper = {'Water': Water, "Tea": Tea}
        if drink_type in drink_mapper.keys():
            if name in [d.name for d in self.drinks_menu]:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            else:
                new_drink = drink_mapper[drink_type](name, portion, brand)
                self.drinks_menu.append(new_drink)
                return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table_mapper = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}
        if table_type in table_mapper.keys():
            if table_number in [t.table_number for t in self.tables_repository]:
                raise Exception(f"Table {table_number} is already in the bakery!")
            else:
                new_table = table_mapper[table_type](table_number, capacity)
                self.tables_repository.append(new_table)
                return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        all_tables = [t for t in self.tables_repository if t.capacity >= number_of_people and not t.is_reserved]
        if all_tables:
            free_table = all_tables[0]
            free_table.is_reserved = True
            free_table.number_of_people += number_of_people
            return f'Table {free_table.table_number} has been reserved for {number_of_people} people'
        else:
            return f'No available table for {number_of_people} people'

    def order_food(self, table_number: int, *foods_names):
        searched_table = None
        for table_obj in self.tables_repository:
            if table_obj.table_number == table_number:
                searched_table = table_obj
        if not searched_table:
            return f"Could not find table {table_number}"
        else:
            ordered = f'Table {table_number} ordered:\n'
            not_ordered = f'{self.name} does not have in the menu:\n'
            for food_name in foods_names:
                if food_name in [f.name for f in self.food_menu]:
                    for food_obj in self.food_menu:
                        if food_obj.name == food_name:
                            ordered += f'{repr(food_obj)}\n'
                            searched_table.food_orders.append(food_obj)
                            self.total_income += food_obj.price
                else:
                    not_ordered += f"{food_name}\n"
            return ordered + not_ordered.rstrip()

    def order_drink(self, table_number: int, *drinks_name):
        searched_table = None
        for table_obj in self.tables_repository:
            if table_obj.table_number == table_number:
                searched_table = table_obj
        if not searched_table:
            return f"Could not find table {table_number}"
        else:
            ordered = f'Table {table_number} ordered:\n'
            not_ordered = f'{self.name} does not have in the menu:\n'
            for drink_name in drinks_name:
                if drink_name in [f.name for f in self.drinks_menu]:
                    for drink_obj in self.drinks_menu:
                        if drink_obj.name == drink_name:
                            ordered += f'{str(drink_obj)}\n'
                            searched_table.drink_orders.append(drink_obj)
                            self.total_income += drink_obj.price
                else:
                    not_ordered += f"{drink_name}\n"
            return ordered + not_ordered.rstrip()

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.table_number == table_number][0]
        foods_bill = sum([f.price for f in table.food_orders])
        drinks_bill = sum([f.price for f in table.drink_orders])
        total_bill = foods_bill + drinks_bill
        table.clear()
        return f'Table: {table_number}\nBill: {total_bill:.2f}'

    def get_free_tables_info(self):
        result = ""
        free_tables = [t for t in self.tables_repository if not t.is_reserved]
        for table_obj in free_tables:
            result += f"{table_obj.free_table_info()}\n"
        return result.rstrip()

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'
