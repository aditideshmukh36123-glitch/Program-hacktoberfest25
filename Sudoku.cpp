#include <bits/stdc++.h>
using namespace std;

#define N 9  // Size of the Sudoku grid

// Function to print the Sudoku grid
void printGrid(int grid[N][N]) {
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to check if placing num at grid[row][col] is valid
bool isSafe(int grid[N][N], int row, int col, int num) {
    // Check row
    for(int x=0; x<N; x++)
        if(grid[row][x] == num) return false;

    // Check column
    for(int x=0; x<N; x++)
        if(grid[x][col] == num) return false;

    // Check 3x3 subgrid
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            if(grid[i+startRow][j+startCol] == num) return false;

    return true; // It's safe to place num
}

// Function to solve Sudoku using backtracking
bool solveSudoku(int grid[N][N]) {
    int row, col;
    bool emptyFound = false;

    // Find an empty cell
    for(row=0; row<N; row++){
        for(col=0; col<N; col++){
            if(grid[row][col] == 0){ // 0 means empty
                emptyFound = true;
                break;
            }
        }
        if(emptyFound) break;
    }

    // If no empty cell, Sudoku is solved
    if(!emptyFound) return true;

    // Try numbers 1 to 9 in the empty cell
    for(int num=1; num<=9; num++){
        if(isSafe(grid, row, col, num)){
            grid[row][col] = num; // Place num

            if(solveSudoku(grid)) // Recur
                return true;

            grid[row][col] = 0; // Backtrack if solution fails
        }
    }

    return false; // Trigger backtracking
}

int main() {
    // 0 represents empty cells
    int grid[N][N] = {
        {5,3,0,0,7,0,0,0,0},
        {6,0,0,1,9,5,0,0,0},
        {0,9,8,0,0,0,0,6,0},
        {8,0,0,0,6,0,0,0,3},
        {4,0,0,8,0,3,0,0,1},
        {7,0,0,0,2,0,0,0,6},
        {0,6,0,0,0,0,2,8,0},
        {0,0,0,4,1,9,0,0,5},
        {0,0,0,0,8,0,0,7,9}
    };

    if(solveSudoku(grid)){
        cout << "Solved Sudoku:\n";
        printGrid(grid);
    } else {
        cout << "No solution exists\n";
    }
    return 0;
}
