from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = self.add_repo()
        self.aquariums = []  # all aquariums (objects).

    @staticmethod
    def add_repo():
        repo_obj = DecorationRepository()
        return repo_obj

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium_mapper = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
        if aquarium_type not in aquarium_mapper:
            return 'Invalid aquarium type.'
        else:
            new_aquarium = aquarium_mapper[aquarium_type](aquarium_name)
            self.aquariums.append(new_aquarium)
            return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == 'Ornament':
            decoration_to_add = Ornament()
        elif decoration_type == 'Plant':
            decoration_to_add = Plant()
        else:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration_to_add)
        return f"Successfully added {decoration_type}."

    def find_aquarium_by_name(self, aquarium_name_):
        for aquarium_obj in self.aquariums:
            if aquarium_obj.name == aquarium_name_:
                return aquarium_obj

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.find_aquarium_by_name(aquarium_name)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        else:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    @staticmethod
    def create_fish_by_type(fish_type_, fish_name_, fish_species_, price_):
        if fish_type_ == 'FreshwaterFish':
            return FreshwaterFish(fish_name_, fish_species_, price_)
        elif fish_type_ == 'SaltwaterFish':
            return SaltwaterFish(fish_name_, fish_species_, price_)
        else:
            return None

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        new_fish = self.create_fish_by_type(fish_type, fish_name, fish_species, price)
        if not new_fish:
            return f"There isn't a fish of type {fish_type}."
        aquarium = self.find_aquarium_by_name(aquarium_name)
        return aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        for fish in aquarium.fish:
            fish.eat()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        total_value = self.calculate_value_of_all_decorations_and_fish(aquarium)
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    @staticmethod
    def calculate_value_of_all_decorations_and_fish(aquarium_obj):
        sum_fish = sum([f.price for f in aquarium_obj.fish])
        sum_decorations = sum([d.price for d in aquarium_obj.decorations])
        return sum_fish + sum_decorations

    def report(self):
        return '\n'.join([str(a) for a in self.aquariums])
