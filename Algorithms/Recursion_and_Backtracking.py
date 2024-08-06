#Study concepts: Recursive algorithms, backtracking techniques.
#Practice: Classic problems like N-Queens, Sudoku solver.
# 1. Recursion
# Definition:

# Recursion is a programming technique where a function calls itself in order to solve a problem. It’s often used to break down complex problems into simpler ones.
# Concepts:

# Base Case: The condition under which the recursion stops.
# Recursive Case: The condition where the function continues to call itself.
# Common Patterns:

# Divide and Conquer: Break the problem into smaller sub-problems, solve each sub-problem, and combine the solutions.
# Tree Traversal: Use recursion to traverse binary trees (e.g., in-order, pre-order, post-order).
# Example Code:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Key Points:

# Ensure that your recursion has a base case to avoid infinite recursion.
# Understand how recursion works with the call stack.
# 2. Backtracking
# Definition:

# Backtracking is an algorithmic technique for solving problems incrementally, by trying out possible solutions and reverting ("backtracking") when a solution path is invalid or not promising.
# Concepts:

# State Space Tree: Represents all possible states of the problem.
# Choice: At each state, decide which choice to make.
# Constraint: Ensure that the choices made are valid.
# Backtrack: Undo the last choice if it leads to an invalid solution.
# Common Patterns:

# Generate and Test: Generate possible solutions and test them.
# Depth-First Search (DFS): Explore all paths from a given state.
# Example Code:

def backtrack(path, choices, result):
    if is_solution(path):
        result.append(path[:])
        return
    for choice in choices:
        if is_valid(path, choice):
            path.append(choice)
            backtrack(path, choices, result)
            path.pop()

def is_solution(path):
    # Define if the path is a solution
    pass

def is_valid(path, choice):
    # Define if adding the choice is valid
    pass




# Classic Problems and Practice
# N-Queens Problem:

# Description: Place N queens on an N x N chessboard such that no two queens threaten each other.
# Approach: Use backtracking to place queens row by row, ensuring no two queens share the same column, row, or diagonal.



def solveNQueens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            results.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)

    results = []
    solve([-1] * n, 0)
    return results

# Sudoku Solver:

# Description: Solve a Sudoku puzzle using a backtracking approach.
# Approach: Try placing numbers in empty cells, backtrack if a number leads to an invalid state, and continue until the board is solved.


def solveSudoku(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or \
               board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = '.'
                    return False
        return True

    solve(board)

# Combination Sum:

# Description: Find all possible combinations of numbers that add up to a target value.
# Approach: Use backtracking to explore all combinations of numbers.

def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if target - candidates[i] >= 0:
                backtrack(i, target - candidates[i], path + [candidates[i]])

    result = []
    backtrack(0, target, [])
    return result


