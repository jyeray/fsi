from random import randint


def randomHeuristic(state):
    return randint(0, 100)


def horizontalHeuristic(state):
    result = 0
    for number in range(1, 7):
        line = {}
        for point in state.board:
            if point[1] == number:
                line[point] = state.board[point]
        result += horizontalLineHeuristic(line, state.moves)
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


def horizontalLineHeuristic(line, moves):
    result = 0
    for point in line:
        inrow = horizontalCount(line, point)
        if line[point] == 'X':
            result += getHorizontalPoints(moves, point, inrow)
        else:
            result -= getHorizontalPoints(moves, point, inrow)
    return result


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
