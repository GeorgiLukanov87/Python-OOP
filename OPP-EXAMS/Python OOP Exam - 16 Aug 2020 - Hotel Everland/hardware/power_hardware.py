from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    TYPE = 'Power'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.TYPE, capacity, memory)
        self.name = name
        self.hardware_type = PowerHardware.TYPE
        self.capacity = int(capacity * 0.25)
        self.memory = int(memory * 1.75)

        self.initial_memory = self.memory
        self.initial_cap = self.capacity
