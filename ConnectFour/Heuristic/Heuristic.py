from random import randint

from DiagonalHeuristic import diagonal_heuristic
from HorizontalHeuristic import horizontal_heuristic
from VerticalHeuristic import vertical_heuristic

from ConnectFour.Heuristic.InverseDiagonalHeuristic import inverse_diagonal_heuristic


def memoize(heuristic):
    memo = {}

    def helper(state, problem_player):
        if str(state.board) not in memo:
            memo[str(state.board)] = heuristic(state, problem_player)
        return memo[str(state.board)]

    return helper


def random_heuristic(state):
    return randint(0, 100)


@memoize
def combined_heuristic(state, problem_player):
    value = horizontal_heuristic(state, problem_player) + vertical_heuristic(state, problem_player) \
            + diagonal_heuristic(state, problem_player) + inverse_diagonal_heuristic(state, problem_player)
    if value == float('inf'):
        value = 100000000
        value -= len(state.board.keys())
    return value
