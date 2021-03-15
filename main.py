board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]


def print_board(bo):
    """Prints the whole Sudoku Board

    Args:
        bo (INT): 2D list of ints
    """

    for i in range(len(bo)):
        if i % 3 == 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0:
                print("| ", end="")

            if j == 8:
                print(str(bo[i][j]) + " |")
            else:
                print(str(bo[i][j]) + " ", end="")
    
    print("- - - - - - - - - - - - -")


def find_empty_spot(bo):
    """finds an empty spot to check for combinations

    Args:
        bo (INT): 2D list of ints
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


def find_valid(bo, num, pos):
    """check for valid number to put in the empty location

    Args:
        bo (INT): 2D list of ints
        num (INT): an integer to match with the empty spots
        pos (INT): the empty spot (containes two values [row, col])
    """

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    """solver function using backtracking

    Args:
        bo (INT): 2D list of ints
    """
    empty = find_empty_spot(bo) # finds an empty spot
    if not empty:
        return True # if thers's no empty spot we're done
    else:
        row, col = empty # otherwise we'll get a row, and col value

    for i in range(1, 10): # the valid values are 1 to 9
        if find_valid(bo, i, (row, col)): 
            bo[row][col] = i # if there's a valid value for the position(row, col) then we place it there

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


print_board(board)
solve(board)
print()
print("Solved Board")
print_board(board)
