from project.helper.validator import Validator


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []  # List to add OBJs by the client !
        self.bill = float(0.0)

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        Validator.raise_if_phone_number_is_invalid(value, 'Invalid phone number!')
        self.__phone_number = value
