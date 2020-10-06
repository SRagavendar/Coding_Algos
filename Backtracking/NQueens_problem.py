"""
Placing queens on a chess board so that no 2 queens threaten each other. N queens for N rows meaning there can only be 1 queen per row.
Eg:
indexes:   0 1 2 3
        0 |0|1|0|0| 1 means a queen is placed, 0 means nothing is placed.
        1 |0|0|0|1|
        2 |1|0|0|0|
        3 |0|0|1|0|
"""
def solve(row_index, board_config, n):
    if row_index >= n:
        return False
    for col_index in range(n):
        test_place_queen = can_place_queen(row_index, col_index, board_config, n)
        if test_place_queen:
            board_config[row_index][col_index] = 1
            if row_index + 1 == n:
                return True
            solved = solve(row_index + 1, board_config, n)
            if solved:
                return True
            else:
                board_config[row_index][col_index] = 0
    return False
def can_place_queen(current_row, current_col, board_config, n):
    for c in range(current_col + 1, n):
        if board_config[current_row][c] == 1:
            return False
    for c in range(0, current_col):
        if board_config[current_row][c] == 1:
            return False

    for r in range(current_row + 1, n):
        if board_config[r][current_col] == 1:
            return False
    for r in range(0, current_row):
        if board_config[r][current_col] == 1:
            return False

    temp_row, temp_col = current_row + 1, current_col - 1
    while temp_col >= 0 and temp_row < n:
        if board_config[temp_row][temp_col] == 1:
            return False
        temp_col -= 1
        temp_row += 1

    temp_row, temp_col = current_row - 1, current_col + 1
    while temp_row >= 0 and temp_col < n:
        if board_config[temp_row][temp_col] == 1:
            return False
        temp_col += 1
        temp_row -= 1

    temp_row, temp_col = current_row + 1, current_col + 1
    while temp_row < n and temp_col < n:
        if board_config[temp_row][temp_col] == 1:
            return False
        temp_row += 1
        temp_col += 1

    temp_row, temp_col = current_row - 1, current_col - 1
    while temp_row >= 0 and temp_col >= 0:
        if board_config[temp_row][temp_col] == 1:
            return False
        temp_row -= 1
        temp_col -= 1
    return True

n = 8
board = [[0] * n for _ in range(n)]
start_row = 0
start_col = 0

result = solve(start_row, board, n)
print(result)
for row in board:
    s = ""
    for c in str(row):
        if c == "1":
            s += "Q"
        elif c == "0":
            s += "-"
        else:
            s += c
    print(s)