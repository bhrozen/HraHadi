import random


class Player:
    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def roll(self):
        roll = random.randint(1, 6)
        if roll == 6:
            roll += self.roll()
        return roll

    def move(self, roll: int):
        new_position = self.position + roll
        if new_position <= 100:
            self.position = new_position
