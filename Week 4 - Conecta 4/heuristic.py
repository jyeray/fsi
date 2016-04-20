from random import randint

def randomHeuristic(state):
    return randint(0, 100)

def horizontalHeuristic(state):
    result = 0
    for point in state.board:
        if state.board[point] == 'X':
            result += horizontalCount(state, point)
    print result
    return result


def horizontalCount(state, point):
    player = state.board[point]
    count = 1
    point = (point[0] + 1, point[1])
    while point in state.board:
        if state.board[point] == player:
            count += 1
            point = (point[0] + 1, point[1])
        else:
            return count
    return count
