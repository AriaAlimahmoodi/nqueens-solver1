import tkinter as tk
from algorithms.genetic import Genetic
from algorithms.csp_mac import solve_n_queens_mac
from algorithms.backtracking import solve_n_queens_bt


def run_backtracking():
    try:
        n = int(entry.get())
        board = [[0] * n for _ in range(n)]
        if solve_n_queens_bt(board, 0, n):
            display_result(board)
        else:
            result_label.config(text="No solution found (Backtracking)")
    except ValueError:
        result_label.config(text="Enter a valid number")





def run_genetic():
    try:
        n = int(entry.get())
        solver = Genetic(n)
        solution = solver.solve()
        if solution:
            board = [[0] * n for _ in range(n)]
            for col, row in enumerate(solution):
                board[row][col] = 1
            display_result(board)
        else:
            result_label.config(text="No solution found (Genetic)")
    except ValueError:
        result_label.config(text="Enter a valid number")




def run_mac():
    try:
        n = int(entry.get())
        solution = solve_n_queens_mac(n)
        if solution:
            board = [[0] * n for _ in range(n)]
            for col, row in solution.items():
                board[row][col] = 1
            display_result(board)
        else:
            result_label.config(text="No solution found (MAC)")
    except ValueError:
        result_label.config(text="Enter a valid number")

def display_result(board):
    for widget in result_frame.winfo_children():
        widget.destroy()
    n = len(board)

    # کوچک‌سازی خانه‌ها برای N بزرگ
    cell_width = 2 if n <= 50 else 1
    cell_height = 1
    font_size = 8 if n <= 50 else 6

    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            cell = tk.Label(result_frame, width=cell_width, height=cell_height,
                            font=("Arial", font_size),
                            bg=color, text="♛" if board[i][j] else "")
            cell.grid(row=i, column=j)


# ---------- GUI ----------
root = tk.Tk()
root.title("N-Queens Solver (Backtracking, Genetic, CSP MAC)")

entry_label = tk.Label(root, text="Enter N (e.g. 8):")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

solve_bt_btn = tk.Button(root, text="Solve with Backtracking", command=run_backtracking)
solve_bt_btn.pack(pady=2)

solve_gen_btn = tk.Button(root, text="Solve with Genetic Algorithm", command=run_genetic)
solve_gen_btn.pack(pady=2)

solve_mac_btn = tk.Button(root, text="Solve with CSP (MAC)", command=run_mac)
solve_mac_btn.pack(pady=2)

result_label = tk.Label(root, text="")
result_label.pack()

result_frame = tk.Frame(root)
result_frame.pack()

root.mainloop()
