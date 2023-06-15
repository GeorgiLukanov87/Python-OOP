from project.car.core.helper import Helper
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = Helper.create_car(car_type, model, speed_limit)
        if model in [c.model for c in self.cars]:
            raise Exception(f'Car {model} is already created!')
        if car:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)
        if driver_name in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")
        if driver not in self.drivers:
            self.drivers.append(driver)
            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = Race(race_name)
        if race_name in [r.name for r in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        if race not in self.races:
            self.races.append(race)
            return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = Helper.search_driver_by_name(driver_name, self.drivers)
        car = Helper.search_last_car_of_car_type(car_type, self.cars)

        if driver.car is None and not car.is_taken:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

        if driver.car is not None and not car.is_taken:
            car.is_taken = True
            driver.car.is_taken = False
            old_car = driver.car.model
            driver.car = car
            return f"Driver {driver.name} changed his car from {old_car} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = Helper.search_race_by_name(race_name, self.races)
        driver = Helper.search_driver_by_name(driver_name, self.drivers)

        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver.name} is already added in {race.name} race."
        race.drivers.append(driver)
        return f"Driver {driver.name} added in {race.name} race."

    def start_race(self, race_name: str):
        race = Helper.search_race_by_name(race_name, self.races)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result, top3_winners_names = Helper.start_race(race)

        Helper.change_stats_by_top3_winners_names(top3_winners_names, self.drivers)
        return result
