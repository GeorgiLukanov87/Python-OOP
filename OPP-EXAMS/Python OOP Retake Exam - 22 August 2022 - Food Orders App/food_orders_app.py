from project.client import Client
from project.helper.validator import Validator
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu = []  # all the meals (objects)!
        self.clients_list = []  # all the clients (objects)!
        self.order = 0

    def register_client(self, client_phone_number: str):
        client = Client(client_phone_number)
        if [c for c in self.clients_list if c.phone_number == client_phone_number]:
            raise Exception('The client has already been registered!')
        self.clients_list.append(client)
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in ['Starter', 'MainDish', 'Dessert']:
                self.menu.append(meal)

    def show_menu(self):
        Validator.raise_if_menu_is_less_than_5_dishes(self.menu, 'The menu is not ready!')
        result = ''
        for meal in self.menu:
            result += meal.details() + '\n'
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        client = None
        # Validate menu before adding items to the client!
        Validator.raise_if_menu_is_less_than_5_dishes(self.menu, 'The menu is not ready!')
        # searching for client , if not in the list -> auto-add it !
        client = Validator.find_client_by_phone_number(client_phone_number, self.clients_list)
        if client is None:
            client = Client(client_phone_number)
        self.clients_list.append(client)
        Validator.raise_if_meal_name_not_in_menu(meal_names_and_quantities, self.menu)
        Validator.raise_if_qnt_is_wrong(meal_names_and_quantities, self.menu)
        self.add_client_order_to_client_shopping_card(client, meal_names_and_quantities)
        print_names = [x.name for x in client.shopping_cart]
        return f"Client {client.phone_number} successfully ordered {', '.join(print_names)} for {client.bill:.2f}lv."

    def add_client_order_to_client_shopping_card(self, client: Client, client_order):
        class_mapper = {
            'Starter': Starter,
            'MainDish': MainDish,
            'Dessert': Dessert,
        }
        meal_names = []
        for meal, qnt in client_order.items():
            Validator.remove_qnt_from_general_menu(self.menu, meal, qnt)

            meal_names.append(meal)
            current_type = [type(obj).__name__ for obj in self.menu if obj.name == meal][0]
            current_price = [obj.price for obj in self.menu if obj.name == meal][0]
            current_meal_obj = class_mapper[current_type](meal, current_price, qnt)

            client.bill += current_price * qnt
            client.shopping_cart.append(current_meal_obj)

    def cancel_order(self, client_phone_number: str):
        client = Validator.find_client_by_phone_number(client_phone_number, self.clients_list)
        if len(client.shopping_cart) <= 0:
            raise Exception('There are no ordered meals!')
        else:
            for obj in client.shopping_cart:
                meal_name = obj.name
                meal_qnt = obj.quantity
                Validator.add_qnt_to_general_menu(self.menu, meal_name, meal_qnt)
        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = Validator.find_client_by_phone_number(client_phone_number, self.clients_list)
        if len(client.shopping_cart) <= 0:
            raise Exception('There are no ordered meals!')
        self.order += 1
        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0

        return f"Receipt #{self.order} with total amount of {total_paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        result = f'Food Orders App has {len(self.menu)} meals on the menu ' \
               f'and {len(self.clients_list)} clients.'
        return result.strip()

