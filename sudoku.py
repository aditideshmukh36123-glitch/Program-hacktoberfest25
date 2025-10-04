# Size of the Sudoku grid
N = 9

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Function to check if placing 'num' at grid[row][col] is valid
def is_safe(grid, row, col, num):
    # Check the row
    if num in grid[row]:
        return False
    
    # Check the column
    for i in range(N):
        if grid[i][col] == num:
            return False
    
    # Check 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

# Function to solve Sudoku using backtracking
def solve_sudoku(grid):
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:  # Empty cell found
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num  # Place number
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack
                return False  # Trigger backtracking
    return True  # Solved

# Example Sudoku grid (0 represents empty cells)
grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve_sudoku(grid):
    print("Solved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists")
