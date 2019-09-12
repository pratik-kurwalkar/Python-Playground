# Program to give random outcome of a two headed dice

import random


class Dice:
    def __init__(self):
        self.rolls = (random.randint(1, 6), random.randint(1, 6))

    def roll(self):
        print(self.rolls)


dice = Dice()
dice.roll()
