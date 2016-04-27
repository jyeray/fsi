from random import randint
from HorizontalHeuristic import horizontalHeuristic
from VerticalHeuristic import verticalHeuristic
from DiagonalHeuristic import diagonalHeuristic
from InverseDiagonalHeuristic import inverseDiagonalHeuristic


def randomHeuristic(state):
    return randint(0, 100)


def combinedHeuristic(state):
    return horizontalHeuristic(state) + verticalHeuristic(state) \
           + diagonalHeuristic(state) + inverseDiagonalHeuristic(state)

