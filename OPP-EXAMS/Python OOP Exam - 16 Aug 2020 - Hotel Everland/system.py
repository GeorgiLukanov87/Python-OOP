from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    def __init__(self):
        ...

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware_to_add = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware_to_add)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware_to_add = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware_to_add)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in [h.name for h in System._hardware]:
            return f"Hardware does not exist"
        else:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        new_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_express_software)
        System._software.append(new_express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in [h.name for h in System._hardware]:
            return f"Hardware does not exist"
        else:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        new_light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_light_software)
        System._software.append(new_light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        if hardware_name in [h.name for h in System._hardware] and \
                software_name in [s.name for s in System._software]:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = []
        software_memory = 0
        software_cap = 0

        for software_el in System._software:
            software_memory += software_el.memory_consumption
            software_cap += software_el.capacity_consumption

        total_memory = sum([m.initial_memory for m in System._hardware])
        total_cap = sum([m.initial_cap for m in System._hardware])

        result.append("System Analysis")
        result.append(f'Hardware Components: {len(System._hardware)}')
        result.append(f'Software Components: {len(System._software)}')

        result.append(f"Total Operational Memory: {software_memory} / "
                      f"{total_memory}")

        result.append(f'Total Capacity Taken: {software_cap} / '
                      f'{total_cap}')

        return "\n".join(result)

    @staticmethod
    def system_split():
        result = []
        for el in System._hardware:
            result.append(f'Hardware Component - {el.name}')

            result.append(f'Express Software Components: '
                          f'{len([x for x in el.software_components if type(x).__name__ == "ExpressSoftware"])}')

            result.append(f'Light Software Components: '
                          f'{len([x for x in el.software_components if type(x).__name__ == "LightSoftware"])}')

            result.append(f'Memory Usage: '
                          f'{sum([mc.memory_consumption for mc in el.software_components])} / {el.initial_memory}')

            result.append(f'Capacity Usage: '
                          f'{sum([mc.capacity_consumption for mc in el.software_components])} / {el.initial_cap}')

            result.append(f'Type: {el.TYPE}')

            if not el.software_components:
                result.append(f'Software Components: None')
            else:
                result.append(f'Software Components: {", ".join([n.name for n in el.software_components])}')

        return '\n'.join(result)
