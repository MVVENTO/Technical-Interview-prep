def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test
print(factorial(5))  # Output: 120


# Recursion is a function that calls itself. It’s often used to solve problems that can be broken down into smaller subproblems.

# 🔧 Example: Factorial of a number
# The factorial of n is n * (n-1) * (n-2) * ... * 1.

# Steps to solve recursion problems:

# Identify the base case (when to stop recursion).
# Identify the recursive case (the function calling itself with modified input).
