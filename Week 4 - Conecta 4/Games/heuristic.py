from random import randint
from HorizontalHeuristic import horizontalHeuristic
from VerticalHeuristic import verticalHeuristic


def randomHeuristic(state):
    return randint(0, 100)


def combinedHeuristic(state):
    result = 0
    result += horizontalHeuristic(state)
    result += verticalHeuristic(state)
    return result
