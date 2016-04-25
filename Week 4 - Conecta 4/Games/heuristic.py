from random import randint
from HorizontalHeuristic import horizontalHeuristic
from VerticalHeuristic import verticalHeuristic
from DiagonalHeuristic import diagonalHeuristic


def randomHeuristic(state):
    return randint(0, 100)


def combinedHeuristic(state):
    result = 0
    result += horizontalHeuristic(state)
    result += verticalHeuristic(state)
    result += diagonalHeuristic(state)
    return result
