class Player:
    added_names = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.check_name(name)

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @staticmethod
    def check_name(name_):
        if name_ not in Player.added_names:
            Player.added_names.append(name_)
        else:
            raise Exception(f'Name {name_} is already used!')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError('Stamina not valid!')
        self.__stamina = value

    def __repr__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
