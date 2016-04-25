from random import randint
from HorizontalHeuristic import horizontalHeuristic
from VerticalHeuristic import verticalHeuristic
from DiagonalHeuristic import diagonalHeuristic
from InverseDiagonalHeuristic import inverseDiagonalHeuristic


def randomHeuristic(state):
    return randint(0, 100)


def combinedHeuristic(state):
    result = 0
    result += horizontalHeuristic(state)
    result += verticalHeuristic(state)
    result += diagonalHeuristic(state)
    result += inverseDiagonalHeuristic(state)
    return result
