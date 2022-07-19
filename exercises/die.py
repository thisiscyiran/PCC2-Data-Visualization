from random import randint

class Die():
    """ simulate Dice """

    def __init__(self, num_sides=6):
        """ initlaize dice attributes """
        self.num_sides = num_sides

    def roll(self):
        """ Create Rolling behavior for dice """
        return randint(1, self.num_sides)
