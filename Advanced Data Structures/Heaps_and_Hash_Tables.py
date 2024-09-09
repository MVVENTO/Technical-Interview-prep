# Heaps in Python
# A heap is a special tree-based data structure that satisfies the heap property:

# Min-heap: The key at the root is the minimum among all keys in the heap, and the same is true for every subtree.
# Max-heap: The key at the root is the maximum, and the same is true for all subtrees.
# In Python, heaps are commonly implemented using the heapq module, which provides a min-heap by default.

# Key Operations for Heaps:
# Inserting an element:

# Use heapq.heappush(heap, item) to add item to the heap and maintain the heap property.
# Time complexity: O(log n).
# Extracting the minimum element:

# Use heapq.heappop(heap) to pop and return the smallest item from the heap.
# Time complexity: O(log n).
# Finding the minimum element without removal:

# Access the smallest element using heap[0].
# Time complexity: O(1).
# Heapify a list:

# Use heapq.heapify(list) to transform a list into a heap.
# Time complexity: O(n).
# Merging heaps:

# Use heapq.merge(*iterables) to merge multiple sorted inputs into a single sorted output.
# Time complexity: O(n log k) (where k is the number of iterables).
# Code Example:

import heapq

# Initialize an empty heap
min_heap = []

# Insert elements into the heap
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)

# Pop the smallest element
min_element = heapq.heappop(min_heap)  # Returns 1

# Peek at the smallest element without popping
smallest = min_heap[0]  # Returns 3


# Tips for Google Interviews:
# Understand that heapq implements a min-heap by default. For max-heap functionality, invert the sign of the values during insertion and popping.
# For problems like Top K Frequent Elements, Merge K Sorted Lists, and Find Median from Data Stream, heaps are commonly used.

# Hash Tables in Python
# A hash table is a data structure that maps keys to values. It uses a hash function to compute an index into an array, where the desired value can be found.

# In Python, hash tables are implemented using dictionaries (dict).

# Key Operations for Hash Tables:
# Inserting/Updating a value:

# Use dict[key] = value to insert or update a key-value pair.
# Time complexity: O(1) average case.
# Accessing a value:

# Use value = dict[key] to retrieve the value associated with key.
# Time complexity: O(1) average case.
# Checking existence of a key:

# Use key in dict to check if a key exists in the hash table.
# Time complexity: O(1) average case.
# Removing a value:

# Use del dict[key] to remove the key-value pair.
# Time complexity: O(1) average case.
# Iterating over keys/values:

# Use for key in dict: to iterate over keys.
# Use for value in dict.values(): to iterate over values.
# Time complexity: O(n).
# Code Example:

# Initialize a hash table
my_dict = {}

# Insert key-value pairs
my_dict['name'] = 'Alice'
my_dict['age'] = 30

# Access a value by key
age = my_dict['age']  # Returns 30

# Check if a key exists
if 'name' in my_dict:
    print("Name exists")

# Delete a key-value pair
del my_dict['age']

# Collision Handling:
# Chaining: Multiple elements at the same index are stored in a linked list.
# Open Addressing: When a collision occurs, another index is found using methods like linear probing or quadratic probing.
# Hash Table Usage in Google Interviews:
# Hash tables are crucial for solving problems involving frequency counts, lookups, two-sum, subarray sums, and deduplication.
# Efficient hash table usage is critical for optimizing space and time complexities.
# Python Dictionary Features:
# Python's dictionary implementation uses an optimized version of hash tables, called hashmaps.
# Python 3.7+ dictionaries maintain insertion order, which can be beneficial for specific problems like LRU Cache implementations.
# Sample Interview Problem Using Heap & Hash Table:
# Problem: Find Top K Frequent Elements
# Given: An array of integers, return the k most frequent elements.

# Use a hash table to count the frequency of each element.
# Use a min-heap to keep track of the top k elements.
# Solution:

import heapq
from collections import Counter

def top_k_frequent(nums, k):
    # Count the frequency of each element
    freq_map = Counter(nums)
    
    # Use a min-heap to store the top k frequent elements
    min_heap = []
    
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Extract the elements from the heap
    return [num for freq, num in min_heap]


# Time Complexity:
# O(n log k) where n is the number of elements in the array and k is the number of top frequent elements.



#################################################################################################################################
# LEETCODE Pactice Questions

# Hash Table Practice:
# Two Sum

# LeetCode #1
# Difficulty: Easy
# Key Concepts: Hash table lookup, array traversal
# Group Anagrams

# LeetCode #49
# Difficulty: Medium
# Key Concepts: Hash table for grouping, sorting, string manipulation
# Subarray Sum Equals K

# LeetCode #560
# Difficulty: Medium
# Key Concepts: Hash table for prefix sums, array manipulation
# Longest Substring Without Repeating Characters

# LeetCode #3
# Difficulty: Medium
# Key Concepts: Sliding window, hash table
# Find Duplicate Subtrees

# LeetCode #652
# Difficulty: Medium
# Key Concepts: Hash table for serialization, tree traversal
# Insert Delete GetRandom O(1)

# LeetCode #380
# Difficulty: Medium
# Key Concepts: Hash table, array operations
# 4Sum II

# LeetCode #454
# Difficulty: Medium
# Key Concepts: Hash table for pairing sums, counting, multiple arrays
# Word Pattern

# LeetCode #290
# Difficulty: Easy
# Key Concepts: Hash table for matching, string manipulation
# Alien Dictionary

# LeetCode #269
# Difficulty: Hard
# Key Concepts: Hash table, topological sorting, graph traversal
# Heap Practice:
# Kth Largest Element in an Array

# LeetCode #215
# Difficulty: Medium
# Key Concepts: Min-heap for finding kth largest, sorting, quickselect
# Top K Frequent Elements

# LeetCode #347
# Difficulty: Medium
# Key Concepts: Hash table, min-heap
# Find Median from Data Stream

# LeetCode #295
# Difficulty: Hard
# Key Concepts: Min-heap, max-heap, running median
# Merge K Sorted Lists

# LeetCode #23
# Difficulty: Hard
# Key Concepts: Min-heap for merging, linked list
# Meeting Rooms II

# LeetCode #253
# Difficulty: Medium
# Key Concepts: Min-heap for interval scheduling
# Task Scheduler

# LeetCode #621
# Difficulty: Medium
# Key Concepts: Max-heap, frequency counting
# Reorganize String

# LeetCode #767
# Difficulty: Medium
# Key Concepts: Max-heap for arranging characters
# Sliding Window Median

# LeetCode #480
# Difficulty: Hard
# Key Concepts: Min-heap, max-heap, sliding window
# Smallest Range Covering Elements from K Lists

# LeetCode #632
# Difficulty: Hard
# Key Concepts: Min-heap for tracking multiple lists, range calculation
# Ugly Number II

# LeetCode #264
# Difficulty: Medium
# Key Concepts: Min-heap for finding numbers with specific properties
# Combination of Hash Tables & Heaps:
# Design Twitter

# LeetCode #355
# Difficulty: Medium
# Key Concepts: Hash table for user relations, heap for news feed sorting
# Number of Visible People in a Queue

# LeetCode #1944
# Difficulty: Hard
# Key Concepts: Stack, heap for visibility







