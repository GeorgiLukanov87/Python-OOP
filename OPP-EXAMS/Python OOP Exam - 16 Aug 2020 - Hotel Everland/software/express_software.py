from project.software.software import Software


class ExpressSoftware(Software):
    TYPE = 'Express'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.TYPE, capacity_consumption, memory_consumption)
        self.name = name
        self.software_type = ExpressSoftware.TYPE
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption * 2
