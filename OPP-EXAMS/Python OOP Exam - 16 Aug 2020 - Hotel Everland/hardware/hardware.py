from abc import ABC
from project.software.software import Software


class Hardware(ABC):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []  # All software's components installed on that hardware!

    def install(self, software: Software):
        if self.capacity >= software.capacity_consumption and self.memory >= software.memory_consumption:
            self.capacity -= software.capacity_consumption
            self.memory -= software.memory_consumption
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.capacity += software.capacity_consumption
            self.memory += software.memory_consumption
