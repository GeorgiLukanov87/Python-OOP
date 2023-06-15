class Validator:

    @staticmethod
    def raise_if_string_is_empty(string: str, error_msg: str):
        if string.strip() == '':
            raise ValueError(error_msg)

    @staticmethod
    def raise_if_phone_number_is_invalid(phone_number: str, error_msg):
        if len([n for n in phone_number if n.isdigit()]) != 10 or \
                phone_number[0] != '0':
            raise ValueError(error_msg)

    @staticmethod
    def raise_if_price_less_or_eq_zero(price: float, error_msg):
        if price <= 0:
            raise ValueError(error_msg)

    @staticmethod
    def raise_if_menu_is_less_than_5_dishes(menu, error_msg):
        if len(menu) < 5:
            raise Exception(error_msg)

    @staticmethod
    def find_client_by_phone_number(phone_number, client_list):
        client = [c for c in client_list if c.phone_number == phone_number]
        if client:
            return client[0]
        return None

    @staticmethod
    def raise_if_meal_name_not_in_menu(client_orders, menu):
        for meal, count in client_orders.items():
            if meal not in [m.name for m in menu]:
                raise Exception(f'{meal} is not on the menu!')

    @staticmethod
    def raise_if_qnt_is_wrong(client_orders, menu):
        all_qnt = [order.quantity for order in menu]
        all_products = [product.name for product in menu]
        all_types = [type(product).__name__ for product in menu]

        result1 = dict(zip(all_products, all_qnt))
        result2 = dict(zip(all_products, all_types))

        for meal, count in client_orders.items():
            if count > result1[meal]:
                raise Exception(f'Not enough quantity of {result2[meal]}: {meal}!')

    @staticmethod
    def remove_qnt_from_general_menu(general_menu, meal, qnt):
        for obj_meal in general_menu:
            if obj_meal.name == meal:
                obj_meal.quantity -= qnt

    @staticmethod
    def add_qnt_to_general_menu(general_menu, meal, qnt):
        for obj in general_menu:
            if obj.name == meal:
                obj.quantity += qnt
