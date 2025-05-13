# algorithms/backtracking.py

def is_safe(board, row, col, n):
    # بررسی ستون‌ها
    for i in range(row):
        if board[i][col] == 1:
            return False

    # بررسی قطر اصلی ↖
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # بررسی قطر فرعی ↗
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens_bt(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_bt(board, row + 1, n):
                return True
            board[row][col] = 0  # backtrack

    return False
