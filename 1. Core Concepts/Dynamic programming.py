# Dynamic programming (DP) solves problems by breaking them down into overlapping subproblems and storing solutions to avoid redundant work.

# 🔧 Example: Fibonacci Sequence (Memoization)

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Test
print(fibonacci(50))  # Output: 12586269025
