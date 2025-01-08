def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            res.append(["".join(board[i]) for i in range(n)])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = 'Q'
            backtrack(row + 1)
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    res, cols, diag1, diag2 = [], set(), set(), set()
    board = [["."] * n for _ in range(n)]
    backtrack(0)
    return res
