from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        if planet not in self.planets:
            self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name: str):
        for planet_obj in self.planets:
            if planet_obj.name == name:
                return planet_obj
