def horizontalHeuristic(state, problem_player):
    result = 0
    for line in range(1, 7):
        colum = 1
        while colum < 8:
            point = (colum, line)
            if point in state.board:
                inrow = horizontalCount(state.board, point)
                if state.board[point] == problem_player:
                    result += getHorizontalPoints(state.moves, point, inrow)
                else:
                    result -= getHorizontalPoints(state.moves, point, inrow)
                colum += inrow
            else:
                colum += 1
    return result


def getHorizontalPoints(moves, point, inrow):
    multiplier = 0
    if inrow == 1:
        return 0
    if inrow == 4:
        return float('inf')
    leftpoint = (point[0] - 1, point[1])
    rightpoint = (point[0] + inrow, point[1])
    if leftpoint in moves:
        multiplier += 2
    if rightpoint in moves:
        multiplier += 2
    return (inrow * multiplier) ** inrow


def horizontalCount(board, point):
    player = board[point]
    count = 1
    point = (point[0] + 1, point[1])
    while point in board:
        if board[point] == player:
            count += 1
            point = (point[0] + 1, point[1])
        else:
            return count
    return count
