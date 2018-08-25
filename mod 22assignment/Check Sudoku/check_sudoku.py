'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def sudoku_ok(line):
    return (len(line) == 9 and sum(line) == sum(set(line)))

def check_sudoku(grid):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    bad_rows = [row for row in grid if not sudoku_ok(row)]
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not sudoku_ok(col)]
    squares = []
    for i in range(9, step=3):
        for j in range(9, step=3):
          square = list(itertools.chain(row[j:j+3] for row in grid[i:i+3]))
          squares.append(square)
    bad_squares = [square for square in squares if not sudoku_ok(square)]
    return not (bad_rows or bad_cols or bad_squares)

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()