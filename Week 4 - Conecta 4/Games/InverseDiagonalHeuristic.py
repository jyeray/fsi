def inverseDiagonalHeuristic(state, problem_player):
    initial_points = {(1, 4), (1, 5), (1, 6), (2, 6), (3, 6), (4, 6)}
    result = 0
    for point in initial_points:
        result += diagonalLineHeuristic(point, state.board, state.moves, problem_player)
    return result


def diagonalLineHeuristic(point, board, moves, problem_player):
    result = 0
    while point in board or point in moves:
        if point in board:
            inrow = diagonalCount(point, board)
            if board[point] == problem_player:
                result += getDiagonalPoints(point, inrow, moves)
            else:
                result -= getDiagonalPoints(point, inrow, moves)
            point = (point[0] + inrow, point[1] - inrow)
        else:
            point = (point[0] + 1, point[1] - 1)
    return result


def diagonalCount(point, board):
    player = board[point]
    point = (point[0] + 1, point[1] - 1)
    count = 1
    while point in board:
        if board[point] == player:
            count += 1
            point = (point[0] + 1, point[1] - 1)
        else:
            return count
    return count


def getDiagonalPoints(point, inrow, moves):
    multiplier = 0
    if inrow == 1:
        return 0
    if inrow == 4:
        return float('inf')
    down_point = (point[0] + inrow, point[1] - inrow)
    up_point = (point[0] - 1, point[1] + 1)
    if up_point in moves:
        multiplier += 2
    if down_point in moves:
        multiplier += 2
    return (inrow * multiplier) ** inrow
