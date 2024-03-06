import sys

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

def is_exist_row(row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False

def is_exist_col(col, num):
    for i in range(9):
        if board[i][col] == num:
            return True
    return False

def is_exist_square(row, col, num):
    row = row // 3
    col = col // 3
    for i in range(3):
        for j in range(3):
            if board[row*3 + i][col*3 + j] == num:
                return True
    return False

def BT(idx):
    if idx == len(blank):
        for line in board:
            print(''.join(map(str, line)))
        sys.exit(0)

    row, col = blank[idx]
    for num in range(1, 10):
        if not is_exist_row(row, num) and not is_exist_col(col, num) and not is_exist_square(row, col, num):
            board[row][col] = num
            BT(idx + 1)
            board[row][col] = 0

    return

BT(0)