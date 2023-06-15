class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player_obj in players:
            if player_obj not in self.players:
                self.players.append(player_obj)
                added_players.append(player_obj.name)
        return f'Successfully added: {", ".join([n for n in added_players])}'

    def add_supply(self, *supplies):
        for el in supplies:
            self.supplies.append(el)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ['Drink', 'Food']:
            return
        else:
            supply = self.search_supply_by_type(sustenance_type, self.supplies)

        if player_name not in [n.name for n in self.players]:
            return
        else:
            player = self.search_player_by_name(player_name, self.players)

        if not player.need_sustenance:
            self.supplies.append(supply)
            return f"{player_name} have enough stamina."
        else:
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def search_supply_by_type(sustenance_type_, all_supplies_):
        for i in range(len(all_supplies_) - 1, -1, -1):
            if type(all_supplies_[i]).__name__ == sustenance_type_:
                return all_supplies_.pop(i)

        else:
            if sustenance_type_ == 'Drink':
                raise Exception("There are no drink supplies left!")
            else:
                raise Exception("There are no food supplies left!")

    @staticmethod
    def search_player_by_name(player_name_, all_players_):
        search_player = [p for p in all_players_ if p.name == player_name_]
        return search_player[0]

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.search_player_by_name(first_player_name, self.players)
        player2 = self.search_player_by_name(second_player_name, self.players)
        if_no_stamina_print = []
        if player1.stamina == 0 or player2.stamina == 0:
            if player1.stamina == 0:
                if_no_stamina_print.append(f'Player {player1.name} does not have enough stamina.')
            if player2.stamina == 0:
                if_no_stamina_print.append(f'Player {player2.name} does not have enough stamina.')
            return '\n'.join(if_no_stamina_print)

        both_players = [player1, player2]
        sorted_players = sorted(both_players, key=lambda x: x.stamina)
        player_turn1, player_turn2 = sorted_players[0], sorted_players[1]

        if player_turn2.stamina - player_turn1.stamina / 2 < 0:
            player_turn2.stamina = 0
            return f'Winner: {player_turn1.name}'
        else:
            player_turn2.stamina -= player_turn1.stamina / 2

        if player_turn1.stamina - player_turn2.stamina / 2 < 0:
            player_turn1.stamina = 0
            return f'Winner: {player_turn2.name}'
        else:
            player_turn1.stamina -= player_turn2.stamina / 2

        both_players_after_fight = [player_turn1, player_turn2]
        sorted_player_after_fight = sorted(both_players_after_fight, key=lambda x: -x.stamina)
        winner = sorted_player_after_fight[0]
        return f"Winner: {winner.name}"

    def next_day(self):
        for player_obj in self.players:
            if player_obj.stamina - (player_obj.age * 2) < 0:
                player_obj.stamina = 0
            else:
                player_obj.stamina -= (player_obj.age * 2)

        for player_obj in self.players:
            food = self.search_supply_by_type('Food', self.supplies)
            if player_obj.stamina + food.energy > 100:
                player_obj.stamina = 100
            else:
                player_obj.stamina += food.energy

            drink = self.search_supply_by_type('Drink', self.supplies)
            if player_obj.stamina + drink.energy > 100:
                player_obj.stamina = 100
            else:
                player_obj.stamina += drink.energy

    def __str__(self):
        result = []
        for player_obj in self.players:
            result.append(str(player_obj))

        for supply_obj in self.supplies:
            result.append(supply_obj.details())

        return '\n'.join(result)
