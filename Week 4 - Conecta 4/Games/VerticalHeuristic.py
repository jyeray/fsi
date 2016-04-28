def verticalHeuristic(state, problem_player):
    result = 0
    for colum in range(1, 8):
        point = (colum, 1)
        if point in state.board:
            result += verticalLineHeuristic(point, state.board, state.moves, problem_player)
    return result


def verticalLineHeuristic(point, board, moves, problem_player):
    result = 0
    while point in board and point[1] < 4:
        inrow = verticalCount(board, point)
        if board[point] == problem_player:
            result += getVerticalPoints(moves, point, inrow)
        else:
            result -= getVerticalPoints(moves, point, inrow)
        point = (point[0], point[1] + inrow)
    return result


def getVerticalPoints(moves, point, inrow):
    multiplier = 0
    if inrow == 1:
        return 0
    if inrow == 4:
        return float('inf')
    uppoint = (point[0], point[1] + inrow)
    if uppoint in moves:
        multiplier += 2
    return (inrow * multiplier) ** inrow


def verticalCount(board, point):
    player = board[point]
    count = 1
    point = (point[0], point[1] + 1)
    while point in board:
        if board[point] == player:
            count += 1
            point = (point[0], point[1] + 1)
        else:
            return count
    return count
