""" 
Find the path for a knight on a chess board such that the knight visits every square only once.
Backtrack cases:
1. Dead end, no more paths (moves to take).
2. Do backtrack and try another move.
Assuming knight can start anywhere brute force approach is required for small values of n.
    Knights can move in L shapes
    For a 5x5 board.
         0 1 2 3 4
    0   | |x|u|x| |
    1   |x| |u| |x|
    2   |l|l|K|r|r|
    3   |x| |d| |x|
    4   | |x|d|x| |
"""

def start_knights_tour(board, n, counter):
    for r in range(n):
        for c in range(n):
            solved = find_tour(r, c, board, n, counter)
            if solved:
                return True
    return False

def find_tour(current_row, current_col, board, n, counter):
    board[current_row][current_col] = counter
    if n*n == counter:
        return True
    possible_moves = get_possible_moves(current_row, current_col, board, n)
    if not possible_moves:
        board[current_row][current_col] = 0
        return False
    while possible_moves:
        move = possible_moves.pop()
        solved = find_tour(move[0], move[1], board, n, counter + 1)
        if solved:
            return True
    board[current_row][current_col] = 0
    return False

def get_possible_moves(current_row, current_column, board_config, n):
    possible_moves = []
    move_up_row = current_row - 2
    move_down_row = current_row + 2
    move_left_column = current_column - 2
    move_right_column = current_column + 2
    if move_up_row >= 0:
        if current_column - 1 >= 0:
            if board_config[move_up_row][current_column - 1] == 0:
                possible_moves.append((move_up_row, current_column - 1))
        if current_column + 1 < n:
            if board_config[move_up_row][current_column + 1] == 0:
                possible_moves.append((move_up_row, current_column + 1))
    if move_down_row < n:
        if current_column - 1 >= 0:
            if board_config[move_down_row][current_column - 1] == 0:
                possible_moves.append((move_down_row, current_column - 1))
        if current_column + 1 < n:
            if board_config[move_down_row][current_column + 1] == 0:
                possible_moves.append((move_down_row, current_column + 1))
    if move_left_column >= 0:
        if current_row - 1 >= 0:
            if board_config[current_row - 1][move_left_column] == 0:
                possible_moves.append((current_row - 1, move_left_column))
        if current_row + 1 < n:
            if board_config[current_row + 1][move_left_column] == 0:
                possible_moves.append((current_row + 1, move_left_column))
    if move_right_column < n:
        if current_row - 1 >= 0:
            if board_config[current_row - 1][move_right_column] == 0:
                possible_moves.append((current_row - 1, move_right_column))
        if current_row + 1 < n:
            if board_config[current_row + 1][move_right_column] == 0:
                possible_moves.append((current_row + 1, move_right_column))
    return possible_moves

n = 5
board = [[0]*n for _ in range(n)]
counter = 1
result = start_knights_tour(board, n, counter)
print(result)
validate = []
for row in board:
    for num in row:
        validate.append(num)
    print(row)
validate.sort()
print("Visited all places: " + str(validate == [x for x in range(1, n*n + 1)]))