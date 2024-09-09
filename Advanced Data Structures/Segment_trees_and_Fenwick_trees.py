# 1. Segment Trees
# Key Concepts of Segment Trees:
# Segment Trees are used to answer range queries efficiently, such as range sums, range minimums, or range maximums.
# They are especially useful when you need to update values in the array and query over a range repeatedly.
# Time complexity: Both building the segment tree and querying/updating it takes O(log n) per operation, and the initial construction takes O(n).
# Segment Tree Operations:
# Construction:

# Build the tree by recursively dividing the array into segments and storing the aggregate value of each segment (e.g., sum or minimum) in tree nodes.
# Time complexity: O(n) for construction.
# Range Query:

# Query a specific range by traversing the segment tree and combining the results of the segments that intersect with the query range.
# Time complexity: O(log n).
# Point Update:

# Update a value in the original array and propagate the change upwards in the segment tree.
# Time complexity: O(log n).
# Segment Tree Implementation in Python:

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)  # Segment tree array
        # Initialize the leaves with array values
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    # Range query from l to r (inclusive)
    def range_query(self, l, r):
        l += self.n  # Shift index to leaf
        r += self.n  # Shift index to leaf
        result = 0
        while l <= r:
            if l % 2 == 1:  # If l is a right child
                result += self.tree[l]
                l += 1
            if r % 2 == 0:  # If r is a left child
                result += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return result

    # Point update at index i with new value
    def point_update(self, i, value):
        i += self.n  # Shift index to leaf
        self.tree[i] = value  # Update the leaf
        # Propagate the change upwards
        i //= 2
        while i > 0:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

# Usage Example:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)
print(seg_tree.range_query(1, 3))  # Sum of elements in range [1, 3] -> 15
seg_tree.point_update(1, 10)  # Update index 1 to value 10
print(seg_tree.range_query(1, 3))  # Sum of elements in range [1, 3] after update -> 22


# Applications of Segment Trees:
# Range Sum Queries: Efficiently compute the sum of elements in a subarray.
# Range Minimum/Maximum Queries: Find the minimum or maximum value within a given range.
# Dynamic Range Queries: Useful when the array undergoes updates frequently and you still need fast query times.
# 2. Fenwick Trees (Binary Indexed Trees)
# Key Concepts of Fenwick Trees:
# Fenwick Tree (Binary Indexed Tree, BIT) is a data structure that provides an efficient way to handle prefix sums and range queries with updates.
# It is space-efficient and allows both updates and prefix sum queries in O(log n) time.
# Unlike Segment Trees, Fenwick Trees are easier to implement but slightly less flexible (e.g., handling only cumulative sums or cumulative minimum/maximum).
# Fenwick Tree Operations:
# Point Update:

# Update a value at an index and propagate the change to the corresponding nodes in the Fenwick Tree.
# Time complexity: O(log n).
# Prefix Sum Query:

# Compute the sum of elements from the start of the array to a given index by querying the corresponding nodes in the Fenwick Tree.
# Time complexity: O(log n).
# Range Sum Query:

# To calculate the sum of a specific range, subtract the prefix sum at the start of the range from the prefix sum at the end of the range.
# Time complexity: O(log n).
# Fenwick Tree Implementation in Python:


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # BIT array (1-indexed)

    # Point update: add value to index i
    def point_update(self, i, value):
        while i <= self.n:
            self.tree[i] += value
            i += i & -i  # Move to the next node

    # Prefix sum query from 1 to i
    def prefix_sum(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i  # Move to the parent node
        return result

    # Range sum query from l to r (inclusive)
    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

# Usage Example:
arr = [1, 3, 5, 7, 9, 11]
fenwick_tree = FenwickTree(len(arr))

# Build the Fenwick Tree with initial values
for i, value in enumerate(arr):
    fenwick_tree.point_update(i + 1, value)

print(fenwick_tree.range_sum(1, 3))  # Sum of elements in range [1, 3] -> 9
fenwick_tree.point_update(2, 5)  # Update index 2 by adding 5
print(fenwick_tree.range_sum(1, 3))  # Sum of elements in range [1, 3] after update -> 14




# Applications of Fenwick Trees:
# Prefix Sum Queries: Efficiently calculate the sum of elements from the start of the array to a given index.
# Range Sum Queries: Compute the sum of a subarray.
# Frequency Counting: Useful in counting the frequency of elements in dynamic arrays.
# Key Considerations:
# Fenwick Trees are simpler to implement than Segment Trees but are slightly less flexible. They excel in use cases where you need to perform range sum queries and point updates efficiently.
# Segment Trees are more powerful when you need to handle a variety of range queries (e.g., range minimum/maximum queries).
# Practice Problems:
# Segment Tree Problems:
# Range Sum Query - Mutable

# LeetCode #307
# Difficulty: Medium
# Range Minimum Query

# LeetCode #315
# Difficulty: Hard
# Range XOR Query

# Description: Implement a Segment Tree for range XOR queries.
# Difficulty: Medium
# Lazy Propagation in Segment Trees (Advanced):

# Efficiently handle range updates and queries (e.g., adding a value to all elements in a range).
# Difficulty: Hard
# Fenwick Tree Problems:
# Range Sum Query

# LeetCode #303
# Difficulty: Easy
# Binary Indexed Tree (Fenwick Tree)

# LeetCode #307
# Difficulty: Medium
# Reverse Pairs

# LeetCode #493
# Difficulty: Hard
# Count of Smaller Numbers After Self

# LeetCode #315
# Difficulty: Hard
