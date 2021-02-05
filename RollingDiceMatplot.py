# 15-10. Practicing Libraries: Try using Matplotlib to make a die-rolling visualization

from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Assume a six-sided die."""
        self.sides = sides

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.sides)
