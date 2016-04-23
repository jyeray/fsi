from random import randint


def randomHeuristic(state):
    return randint(0, 100)


def horizontalHeuristic(state):
    result = 0
    for line in range(1, 7):
        colum = 1
        while colum < 8:
            point = (colum, line)
            if point in state.board:
                inrow = horizontalCount(state.board, point)
                if state.board[point] == 'X':
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


def horizontalCount(line, point):
    player = line[point]
    count = 1
    point = (point[0] + 1, point[1])
    while point in line:
        if line[point] == player:
            count += 1
            point = (point[0] + 1, point[1])
        else:
            return count
    return count


def verticalHeuristic(state):
    result = 0
    for colum in range(1, 8):
        point = (colum, 1)
        if point in state.board:
            result += verticalLineHeuristic(point, state.board, state.moves)
    return result


def verticalLineHeuristic(point, board, moves):
    result = 0
    while point in board and point[1] < 4:
        inrow = verticalCount(board, point)
        if board[point] == 'X':
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
