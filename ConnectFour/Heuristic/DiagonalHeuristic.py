def diagonal_heuristic(state, problem_player):
    initial_points = {(1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1)}
    result = 0
    for point in initial_points:
        result += diagonal_line_heuristic(point, state.board, state.moves, problem_player)
    return result


def diagonal_line_heuristic(point, board, moves, problem_player):
    result = 0
    while point in board or point in moves:
        if point in board:
            in_row = diagonal_count(point, board)
            if board[point] == problem_player:
                result += get_diagonal_points(point, in_row, moves)
            else:
                result -= get_diagonal_points(point, in_row, moves)
            point = (point[0] + in_row, point[1] + in_row)
        else:
            point = (point[0] + 1, point[1] + 1)
    return result


def diagonal_count(point, board):
    player = board[point]
    point = (point[0] + 1, point[1] + 1)
    count = 1
    while point in board:
        if board[point] == player:
            count += 1
            point = (point[0] + 1, point[1] + 1)
        else:
            return count
    return count


def get_diagonal_points(point, in_row, moves):
    multiplier = 0
    if in_row == 1:
        return 0
    if in_row == 4:
        return float('inf')
    up_point = (point[0] + in_row, point[1] + in_row)
    down_point = (point[0] - 1, point[1] - 1)
    if up_point in moves:
        multiplier += 2
    if down_point in moves:
        multiplier += 2
    return (in_row * multiplier) ** in_row
