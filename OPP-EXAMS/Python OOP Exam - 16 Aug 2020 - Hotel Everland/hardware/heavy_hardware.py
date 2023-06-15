from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    TYPE = 'Heavy'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.TYPE, capacity, memory)
        self.name = name
        self.hardware_type = HeavyHardware.TYPE
        self.capacity = capacity * 2
        self.memory = int(memory * 0.75)

        self.initial_memory = self.memory
        self.initial_cap = self.capacity

