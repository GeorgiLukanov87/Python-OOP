from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet


class Validator:
    @staticmethod
    def create_astro_by_type_and_name(type_, name_):
        astronauts_types_mapper = {
            'Meteorologist': Meteorologist, 'Geodesist': Geodesist, 'Biologist': Biologist, }

        if type_ not in astronauts_types_mapper.keys():
            raise Exception('Astronaut type is not valid!')

        astro_obj = astronauts_types_mapper[type_](name_)
        return astro_obj

    @staticmethod
    def create_planet_by_name_items(planet_name_, items_):
        new_planet = Planet(planet_name_)
        new_planet.items.extend(items_.split(', '))
        return new_planet
