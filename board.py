from player import Player


class PlayDesk:
    def __init__(self):
        self.snake_and_ladder = {
            2: 38, 7: 14, 8: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94,
            16: 6, 46: 26, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80
        }

    def rules(self, position: int):
        if position in self.snake_and_ladder:
            return self.snake_and_ladder[position]
        return position

    @staticmethod
    def check_positions(players: list, player: Player):
        for p in players:
            if p.position == player.position and player.name != p.name:
                return p
        return None
