import tkinter as tk
from tkinter import ttk

sudoku_board = [
    [6, 1, 4, 8, 3, 5, 9, 1, 2],
    [0, 0, 8, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 6, 7, 8, 0],
    [0, 6, 1, 3, 0, 0, 0, 0, 0],
    [3, 0, 0, 7, 0, 0, 0, 2, 6],
    [0, 8, 0, 5, 6, 0, 3, 0, 0],
    [0, 0, 2, 0, 0, 8, 0, 9, 0],
    [8, 9, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 6, 0, 5, 2, 0, 7, 8],
]

def draw_sudoku_board(canvas):
    # Draw the lines for the grid
    for i in range(10):
        if i % 3 == 0:
            linewidth = 2
        else:
            linewidth = 1
        canvas.create_line(i * cell_size, 0, i * cell_size, board_size, width=linewidth)
        canvas.create_line(0, i * cell_size, board_size, i * cell_size, width=linewidth)

    # Draw the numbers on the board
    for row in range(9):
        for col in range(9):
            cell_value = sudoku_board[row][col]
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size

            if cell_value != 0:
                canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2,
                                   text=str(cell_value), font=('Arial', 14))
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill='light gray')

def solve_sudoku():
    empty_cell = find_empty_cell()
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(row, col, num):
            sudoku_board[row][col] = num

            if solve_sudoku():
                return True

            sudoku_board[row][col] = 0

    return False

def find_empty_cell():
    for row in range(9):
        for col in range(9):
            if sudoku_board[row][col] == 0:
                return row, col
    return None

def is_valid_move(row, col, num):
    for i in range(9):
        if sudoku_board[row][i] == num or sudoku_board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku_board[start_row + i][start_col + j] == num:
                return False

    return True

def is_sudoku_solvable():
    return solve_sudoku()

def solve_button_clicked():
    if is_sudoku_solvable():
        draw_sudoku_board(canvas)
    else:
        window = tk.Toplevel(root)
        window.title("Error")
        window.geometry("300x100")
        window.resizable(False, False)
        tk.Label(window, text="The Sudoku board is not solvable.", font=('Arial', 14)).pack()
        tk.Button(window, text="OK", command=window.destroy, font=('Arial', 14)).pack()
        
        print("The Sudoku board is not solvable.")


# Size of each cell in the Sudoku grid
cell_size = 50

# Size of the Sudoku board
board_size = cell_size * 9

# Create the Tkinter window
root = tk.Tk()
root.title("Sudoku Board")

# Create a Canvas widget
canvas = tk.Canvas(root, width=board_size, height=board_size)
canvas.pack()

# Draw the Sudoku board
draw_sudoku_board(canvas)

# Create the Solve button
solve_button = ttk.Button(root, text="Solve", command=solve_button_clicked, style="Custom.TButton")
solve_button.pack()

# Define a custom style for the button
style = ttk.Style()
style.configure(
    "Custom.TButton", 
    font=('Arial', 12, 'bold'), 
    foreground="black", 
    background="white",
    width=12,
    padding=10,
    border=4,
)

# Run the Tkinter main loop
root.mainloop()
# print_board(sudoku_board)
# solve(sudoku_board)
# print()
# print("Solved Board")
# print_board(sudoku_board)
