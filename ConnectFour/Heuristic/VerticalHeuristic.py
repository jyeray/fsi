def vertical_heuristic(state, problem_player):
    result = 0
    for column in range(1, 8):
        point = (column, 1)
        if point in state.board:
            result += vertical_line_heuristic(point, state.board, state.moves, problem_player)
    return result


def vertical_line_heuristic(point, board, moves, problem_player):
    result = 0
    while point in board and point[1] < 4:
        in_row = vertical_count(board, point)
        if board[point] == problem_player:
            result += get_vertical_points(moves, point, in_row)
        else:
            result -= get_vertical_points(moves, point, in_row)
        point = (point[0], point[1] + in_row)
    return result


def vertical_count(board, point):
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


def get_vertical_points(moves, point, in_row):
    multiplier = 0
    if in_row == 1:
        return 0
    if in_row == 4:
        return float('inf')
    up_point = (point[0], point[1] + in_row)
    if up_point in moves:
        multiplier += 2
    return (in_row * multiplier) ** in_row
