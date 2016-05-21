def horizontal_heuristic(state, problem_player):
    result = 0
    for line in range(1, 7):
        column = 1
        while column < 8:
            point = (column, line)
            if point in state.board:
                in_row = horizontal_count(state.board, point)
                if state.board[point] == problem_player:
                    result += get_horizontal_points(state.moves, point, in_row)
                else:
                    result -= get_horizontal_points(state.moves, point, in_row)
                column += in_row
            else:
                column += 1
    return result


def horizontal_count(board, point):
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


def get_horizontal_points(moves, point, in_row):
    multiplier = 0
    if in_row == 1:
        return 0
    if in_row == 4:
        return float('inf')
    left_point = (point[0] - 1, point[1])
    right_point = (point[0] + in_row, point[1])
    if left_point in moves:
        multiplier += 2
    if right_point in moves:
        multiplier += 2
    return (in_row * multiplier) ** in_row
