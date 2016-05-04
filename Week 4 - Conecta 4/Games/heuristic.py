from random import randint
from HorizontalHeuristic import horizontalHeuristic
from VerticalHeuristic import verticalHeuristic
from DiagonalHeuristic import diagonalHeuristic
from InverseDiagonalHeuristic import inverseDiagonalHeuristic


def memoize(heuristic):
    memo = {}

    def helper(state, problem_player):
        if str(state.board) not in memo:
            memo[str(state.board)] = heuristic(state, problem_player)
        return memo[str(state.board)]

    return helper


def randomHeuristic(state):
    return randint(0, 100)


@memoize
def combinedHeuristic(state, problem_player):
    value = horizontalHeuristic(state, problem_player) + verticalHeuristic(state, problem_player) \
           + diagonalHeuristic(state, problem_player) + inverseDiagonalHeuristic(state, problem_player)
    if value == float('inf'):
        value = 100000000
        value -= len(state.board.keys())
    return value
