class DecorationRepository:
    def __init__(self):
        self.decorations = []  # contain all decorations (objects).

    def add(self, decoration):  # Add Obj!
        self.decorations.append(decoration)

    def remove(self, decoration):  # Remove Obj!
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        decorations_founds = [d for d in self.decorations if type(d).__name__ == decoration_type]
        if decorations_founds:
            first_decoration_found = decorations_founds[0]
            return first_decoration_found
        return 'None'
