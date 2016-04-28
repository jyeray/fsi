from random import randint
from HorizontalHeuristic import horizontalHeuristic
from VerticalHeuristic import verticalHeuristic
from DiagonalHeuristic import diagonalHeuristic
from InverseDiagonalHeuristic import inverseDiagonalHeuristic


def randomHeuristic(state):
    return randint(0, 100)


def combinedHeuristic(state, problem_player):
    return horizontalHeuristic(state, problem_player) + verticalHeuristic(state, problem_player) \
           + diagonalHeuristic(state, problem_player) + inverseDiagonalHeuristic(state, problem_player)

