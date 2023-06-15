from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []  # all the horses (objects).
        self.jockeys = []  # all the jockeys (objects).
        self.horse_races = []  # all the horse races (objects).

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        new_horse = self.create_horse_by_type(horse_type, horse_name, horse_speed)
        if new_horse:
            if horse_name not in [h.name for h in self.horses]:
                self.horses.append(new_horse)
                return f"{horse_type} horse {horse_name} is added."
            else:
                raise Exception(f"Horse {horse_name} has been already added!")

    @staticmethod
    def create_horse_by_type(horse_type_, horse_name_, horse_speed_):
        if horse_type_ == 'Appaloosa':
            return Appaloosa(horse_name_, horse_speed_)
        elif horse_type_ == 'Thoroughbred':
            return Thoroughbred(horse_name_, horse_speed_)
        else:
            return None

    def add_jockey(self, jockey_name: str, age: int):
        new_jockey = Jockey(jockey_name, age)
        if jockey_name not in [j.name for j in self.jockeys]:
            self.jockeys.append(new_jockey)
            return f'Jockey {jockey_name} is added.'
        else:
            raise Exception(f'Jockey {jockey_name} has been already added!')

    def create_horse_race(self, race_type: str):
        new_race = HorseRace(race_type)
        if race_type not in [r.race_type for r in self.horse_races]:
            self.horse_races.append(new_race)
            return f'Race {race_type} is created.'
        else:
            raise Exception(f"Race {race_type} has been already created!")

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.search_jockey_by_name(jockey_name, self.jockeys)
        horse = self.search_horse_by_type(horse_type, self.horses)

        if jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'
        else:
            jockey.horse = horse
            horse.is_taken = True
            return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    @staticmethod
    def search_jockey_by_name(jockey_name_, all_jockeys_):
        search_jockey = [j for j in all_jockeys_ if j.name == jockey_name_]
        if not search_jockey:
            raise Exception(f"Jockey {jockey_name_} could not be found!")
        else:
            return search_jockey[0]

    @staticmethod
    def search_horse_by_type(horse_type_, all_horses_):
        search_horse = [h for h in all_horses_ if type(h).__name__ == horse_type_ and not h.is_taken]
        if not search_horse:
            raise Exception(f"Horse breed {horse_type_} could not be found!")
        else:
            return search_horse[-1]

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.search_race_by_type(race_type, self.horse_races)
        jockey = self.search_jockey_by_name(jockey_name, self.jockeys)
        if jockey.horse is None:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')
        if jockey not in race.jockeys:
            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."
        else:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'

    @staticmethod
    def search_race_by_type(race_type_, all_races_):
        search_race = [r for r in all_races_ if r.race_type == race_type_]
        if search_race:
            return search_race[0]
        else:
            raise Exception(f"Race {race_type_} could not be found!")

    def start_horse_race(self, race_type: str):
        race = self.search_race_by_type(race_type, self.horse_races)
        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        winner = sorted(race.jockeys, key=lambda x: -x.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of " \
               f"{winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
