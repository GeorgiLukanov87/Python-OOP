from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Helper:
    @staticmethod
    def create_car(car_type, car_model, speed_limit):
        car_mapper = {'SportsCar': SportsCar, 'MuscleCar': MuscleCar}
        if car_type == 'SportsCar':
            return car_mapper[car_type](car_model, speed_limit)
        elif car_type == 'MuscleCar':
            return car_mapper[car_type](car_model, speed_limit)

    @staticmethod
    def search_last_car_of_car_type(car_type, list_of_cars):
        car = [car for car in list(reversed(list_of_cars))
               if type(car).__name__ == car_type and not car.is_taken]

        if not car:
            raise Exception(f"Car {car_type} could not be found!")
        return car[0]

    @staticmethod
    def search_driver_by_name(driver_name, list_of_drivers):
        for driver_obj in list_of_drivers:
            if driver_obj.name == driver_name:
                return driver_obj

        raise Exception(f'Driver {driver_name} could not be found!')

    @staticmethod
    def search_race_by_name(race_name, list_of_races):
        for race_obj in list_of_races:
            if race_obj.name == race_name:
                return race_obj

        raise Exception(f"Race {race_name} could not be found!")

    @staticmethod
    def start_race(race):
        drivers = [racer for racer in race.drivers]
        drivers_speed = [driver.car.speed_limit for driver in drivers]
        drivers_names = [driver.name for driver in drivers]

        drivers_dict = dict(zip(drivers_names, drivers_speed))
        sorted_drivers = sorted(drivers_dict.items(), key=lambda x: -x[1])

        winners_name = []
        result = ''
        for driver, speed in list(sorted_drivers)[:3]:
            result += f"Driver {driver} wins the {race.name} race with a speed of {speed}.\n"
            winners_name.append(driver)
        return result.strip(), winners_name

    @staticmethod
    def change_stats_by_top3_winners_names(top3_drivers, all_drivers):
        while top3_drivers:
            current_driver_name = top3_drivers.pop()
            for driver_obj in all_drivers:
                if driver_obj.name == current_driver_name:
                    driver_obj.number_of_wins += 1
