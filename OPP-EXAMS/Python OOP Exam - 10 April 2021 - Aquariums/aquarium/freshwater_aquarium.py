from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)
        self.name = name
        self.capacity = self.INITIAL_CAPACITY

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if self.capacity == 0:
            return f"Not enough capacity."
        if type(fish).__name__ == 'FreshwaterFish':
            self.fish.append(fish)
            self.capacity -= 1
            return f"Successfully added {type(fish).__name__} to {self.name}."
        else:
            return 'Water not suitable.'

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)

    def feed(self):
        for fish_obj in self.fish:
            fish_obj.eat()

    def __str__(self):
        fish_names = [f.name for f in self.fish]
        if not fish_names:
            fish_names = ['none']
        result = f"{self.name}:\n"
        result += f"Fish: {' '.join(fish_names)}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result
