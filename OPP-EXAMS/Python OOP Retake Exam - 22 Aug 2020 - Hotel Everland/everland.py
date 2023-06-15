from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_sum = 0
        for room in self.rooms:
            total_sum += room.expenses + room.room_cost
        return f"Monthly consumption: {total_sum:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= (room.expenses + room.room_cost)
                result.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return '\n'.join(result)

    def status(self):
        total_population = sum([p.members_count for p in self.rooms])
        result = [f'Total population: {total_population}']
        for room in self.rooms:
            child_exp = sum([c.cost for c in room.children]) * 30
            if not child_exp:
                child_exp = 0
            current_budget = room.budget
            result.append(f'{room.family_name} with {room.members_count} members. '
                          f'Budget: {current_budget:.2f}$, Expenses: {room.expenses:.2f}$')

            for index, child in enumerate(room.children):
                result.append(f'--- Child {index + 1} monthly cost: {room.children[index].cost*30:.2f}$')

            result.append(f'--- Appliances monthly cost: '
                          f'{(room.expenses - child_exp):.2f}$')

        return '\n'.join(result)
















