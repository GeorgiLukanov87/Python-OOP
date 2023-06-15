from abc import ABC, abstractmethod

from project.helper.validator import Validator


class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, 'Name cannot be an empty string!')
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_price_less_or_eq_zero(value, 'Invalid price!')
        self.__price = value

    @abstractmethod
    def details(self):
        ...



