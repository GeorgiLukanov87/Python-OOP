from project.astronaut.astronaut_repository import AstronautRepository
from project.helper.validator import Validator

from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.mission_completed = 0
        self.mission_failed = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        new_astronaut = Validator.create_astro_by_type_and_name(astronaut_type, name)

        for astro_obj in self.astronaut_repository.astronauts:
            if astro_obj.name == name:
                return f"{name} is already added."
        self.astronaut_repository.astronauts.append(new_astronaut)
        return f'Successfully added {new_astronaut.__class__.__name__}: {new_astronaut.name}.'

    def add_planet(self, name: str, items: str):
        new_planet = Validator.create_planet_by_name_items(name, items)

        for planet_obj in self.planet_repository.planets:
            if planet_obj.name == name:
                return f"{planet_obj.name} is already added."
        self.planet_repository.planets.append(new_planet)
        return f'Successfully added Planet: {new_planet.name}.'

    def retire_astronaut(self, name: str):
        current_astronaut = self.astronaut_repository.find_by_name(name)

        if current_astronaut:
            self.astronaut_repository.remove(current_astronaut)
            return f'Astronaut {current_astronaut.name} was retired!'
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        AMOUNT = 10
        for astro_obj in self.astronaut_repository.astronauts:
            astro_obj.increase_oxygen(AMOUNT)

    def send_on_mission(self, planet_name: str):
        if planet_name not in [planet.name for planet in self.planet_repository.planets]:
            raise Exception("Invalid planet name!")

        planet = self.planet_repository.find_by_name(planet_name)
        astros_need_5 = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        sorted_astros = sorted(astros_need_5, key=lambda x: -x.oxygen)

        if not astros_need_5:
            self.mission_failed += 1
            raise Exception("You need at least one astronaut to explore the planet!")

        counter_astros = 1
        for astro in sorted_astros[:5]:
            while 'none' in astro.backpack:
                astro.backpack.remove('none')
            while True:
                if astro.oxygen <= 0 or not planet.items:
                    break
                astro.backpack.append(planet.items.pop())
                astro.breathe()
                if astro.oxygen <= 0:
                    counter_astros += 1
                    astro.oxygen = 0

        if planet.items:
            self.mission_failed += 1
            return 'Mission is not completed.'

        self.mission_completed += 1
        return f'Planet: {planet.name} was explored. {counter_astros} astronauts participated in collecting items.'

    def report(self):
        result = f"{self.mission_completed} successful missions!\n"
        result += f'{self.mission_failed} missions were not completed!\n'
        result += "Astronauts' info:\n"

        for astro in self.astronaut_repository.astronauts:
            result += str(astro)

        return result.strip()
