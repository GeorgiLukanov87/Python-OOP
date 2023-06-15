from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)
        self.is_taken = False

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not self.MIN_SPEED_LIMIT <= value <= self.MAX_SPEED_LIMIT:
            raise ValueError(f'Invalid speed limit! Must be between'
                             f' {self.MIN_SPEED_LIMIT} and '
                             f'{self.MAX_SPEED_LIMIT}!')
        self.__speed_limit = value
