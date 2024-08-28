# 1. Memoization Example: Fibonacci Sequence
# Memoization involves solving the problem recursively and storing results to avoid redundant computations.
# Memoization for Fibonacci Sequence

def fibonacci_memo(n, memo={}):
    # Base cases
    if n <= 1:
        return n
    # Check if result is in memo
    if n in memo:
        return memo[n]
    # Compute and store the result
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Example usage
print(fibonacci_memo(10))  # Output: 55


#   2. Tabulation Example: Fibonacci Sequence
# Tabulation involves building up a solution iteratively and storing results in a table.

# Tabulation for Fibonacci Sequence

def fibonacci_tab(n):
    # Base cases
    if n <= 1:
        return n
    # Initialize table with base cases
    fib = [0] * (n + 1)
    fib[1] = 1
    # Fill the table
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# Example usage
print(fibonacci_tab(10))  # Output: 55


#   3. Knapsack Problem (0/1 Knapsack)
# Memoization Approach
# Memoization for 0/1 Knapsack Problem

def knapsack_memo(weights, values, capacity):
    def dp(n, w):
        # Base cases
        if n == 0 or w == 0:
            return 0
        # Check if result is in memo
        if (n, w) in memo:
            return memo[(n, w)]
        # Exclude or include the item
        if weights[n-1] > w:
            result = dp(n-1, w)
        else:
            result = max(dp(n-1, w), values[n-1] + dp(n-1, w - weights[n-1]))
        memo[(n, w)] = result
        return result

    memo = {}
    return dp(len(weights), capacity)

# Example usage
weights = [1, 2, 3]
values = [60, 100, 120]
capacity = 5
print(knapsack_memo(weights, values, capacity))  # Output: 220


# Tabulation Approach
# Tabulation for 0/1 Knapsack Problem

def knapsack_tab(weights, values, capacity):
    n = len(weights)
    # Initialize table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

# Example usage
weights = [1, 2, 3]
values = [60, 100, 120]
capacity = 5
print(knapsack_tab(weights, values, capacity))  # Output: 220


# 4. Longest Increasing Subsequence (LIS)
# Memoization Approach
# Memoization for Longest Increasing Subsequence

def lis_memo(arr):
    def dp(i):
        if i == len(arr):
            return 0
        if i in memo:
            return memo[i]
        length = 1
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                length = max(length, 1 + dp(j))
        memo[i] = length
        return length

    memo = {}
    return max(dp(i) for i in range(len(arr)))

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis_memo(arr))  # Output: 6


# Tabulation Approach
# Tabulation for Longest Increasing Subsequence

def lis_tab(arr):
    n = len(arr)
    if n == 0:
        return 0
    # Initialize LIS values for all indexes
    lis = [1] * n
    # Build the LIS array
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis_tab(arr))  # Output: 6


# Summary
# Memoization is a top-down approach where you use recursion and store results in a data structure to avoid redundant calculations.
# Tabulation is a bottom-up approach where you iteratively build up the solution and store intermediate results in a table.
# Common Problems: Practice with problems like Knapsack and LIS helps solidify your understanding of dynamic programming techniques.
# Mastering these examples will help you effectively solve dynamic programming problems in technical interviews.
