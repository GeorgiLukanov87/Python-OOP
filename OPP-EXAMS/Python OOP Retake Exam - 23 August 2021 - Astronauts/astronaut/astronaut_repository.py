from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []  # OJBs of Astronauts !

    def add(self, astronaut: Astronaut):
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astro_obj in self.astronauts:
            if astro_obj.name == name:
                return astro_obj
