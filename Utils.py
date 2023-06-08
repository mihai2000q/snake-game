import random
from enum import Enum

from Constants import *


class Direction(Enum):
    UP = (0, 20)
    DOWN = (0, -20)
    LEFT = (-20, 0)
    RIGHT = (20, 0)

    def __reversed__(self):
        if self.value == Direction.UP.value:
            return Direction.DOWN
        elif self.value == Direction.LEFT.value:
            return Direction.RIGHT
        elif self.value == Direction.RIGHT.value:
            return Direction.LEFT
        else:
            return Direction.UP


def getDistance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras's Theorem
    return distance


def getRandomFoodPos():
    x = random.randint(round(- WIDTH / 2 + FOOD_SIZE), round(WIDTH / 2 - FOOD_SIZE))
    y = random.randint(round(- HEIGHT / 2 + FOOD_SIZE), round(HEIGHT / 2 - FOOD_SIZE))
    return x, y
