# # Fundamentals

# # Understand the basics:
# # Search: The process of finding a specific element or value within a collection of data.
# # Sorting: The process of arranging elements in a specific order (ascending, descending).
# # Know the importance:
# # Search and sort are core operations in computer science, influencing the efficiency of many applications.
# # They're often used in database queries, data analysis, and optimization problems.
# # Focus on time and space complexity:
# # Big O notation: Describes the performance of an algorithm as the input size grows.
# # Time complexity: How the running time of an algorithm increases with the input size.
# # Space complexity: How much additional memory an algorithm needs to run.
# # Essential Search Algorithms

# # Linear Search:
# # How it works: Sequentially checks each element until a match is found.
# # Time complexity: O(n) in the worst case.
# # Best for: Small unsorted datasets or when a match is likely to be near the beginning.
# # Binary Search:
# # How it works: Repeatedly divides a sorted dataset in half, eliminating half the data with each comparison.
# # Time complexity: O(log n) in the worst case.
# # Best for: Large sorted datasets.
# # Hash Tables (for searching within data structures):
# # How it works: Uses a hash function to compute an index into an array of buckets or slots, where desired values are stored.
# # Time complexity: O(1) on average for insertion, deletion, and search, but O(n) in the worst case due to collisions.
# # Best for: Fast search, insert, and delete operations when frequent access is needed.
# # Essential Sorting Algorithms

# # Bubble Sort:
# # How it works: Repeatedly swaps adjacent elements if they are in the wrong order.
# # Time complexity: O(n^2) in the worst and average cases.
# # Best for: Educational purposes or very small datasets.
# # Insertion Sort:
# # How it works: Builds a sorted subarray one element at a time.
# # Time complexity: O(n^2) in the worst and average cases, but can be faster with nearly sorted data.
# # Best for: Small datasets or nearly sorted data.
# # Merge Sort:
# # How it works: Divides the input into smaller subarrays, sorts them recursively, and merges the sorted subarrays back together.
# # Time complexity: O(n log n) in all cases.
# # Best for: General-purpose sorting with guaranteed performance.
# # Quick Sort:
# # How it works: Selects a 'pivot' element, partitions the array around the pivot, and sorts the subarrays recursively.
# # Time complexity: O(n log n) on average, but can degrade to O(n^2) in the worst case.
# # Best for: Often the fastest in practice, but can have worst-case performance issues.
# # Heap Sort:
# # How it works: Builds a max-heap from the input, repeatedly extracts the maximum element to build the sorted array.
# # Time complexity: O(n log n) in all cases.
# # Best for: Guaranteed O(n log n) performance and in-place sorting.
# # Advanced Topics

# # Variations of Quick Sort:
# # 3-way Quick Sort: Handles duplicates efficiently.
# # Randomized Quick Sort: Reduces the likelihood of worst-case scenarios.
# # Specialized Sorting Algorithms:
# # Radix Sort: Sorts integers based on their digits.
# # Counting Sort: Sorts integers within a specific range.
# # External Sorting: Handles data too large to fit in memory.
# # Distributed Sorting: Sorts data across multiple machines.
# # Tips for the Interview

# # Know the trade-offs: Explain when to choose one algorithm over another based on the data and constraints.
# # Practice implementation: Be prepared to write code for basic algorithms like linear/binary search, bubble sort, insertion sort.
# # Analyze complexity: Clearly articulate the time and space complexity of algorithms.
# # Consider edge cases: Think about empty inputs, duplicate values, or very large datasets.
# # Communicate effectively: Explain your thought process, ask clarifying questions, and be open to feedback.
# # Remember:

# # Google values problem-solving skills. Demonstrate your understanding of algorithms and your ability to apply them to real-world situations.
# # Practice makes perfect. The more you practice implementing and analyzing algorithms, the more confident you'll be during the interview.
# # Additional resources

# # Websites:
# # GeeksforGeeks
# # LeetCode
# # HackerRank
# # Books:
# # "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
# # "Cracking the Coding Interview" by Gayle Laakmann McDowell
# # I hope this helps! Good luck with your Google technical interview!



# Search Algorithms

# Linear Search

# 704. Binary Search: While this is titled Binary Search, it's an excellent starting point to grasp the core concept of searching and can also be solved using a Linear Search approach (though less efficiently).
# 278. First Bad Version: This problem requires you to find the first occurrence of a specific element in a sorted array, similar to Linear Search, but with an added twist.
# 162. Find Peak Element: This involves finding a 'peak' in an array, requiring a modified search approach, which can help solidify your understanding of search algorithms.
# Binary Search

# 35. Search Insert Position: A classic Binary Search problem where you need to find the index to insert an element to maintain a sorted array.
# 33. Search in Rotated Sorted Array: A more challenging Binary Search problem where the array is rotated, testing your ability to adapt the algorithm to a modified scenario.
# 81. Search in Rotated Sorted Array II: Similar to the previous problem but with duplicates, further enhancing your understanding of Binary Search edge cases.
# Hash Tables

# 1. Two Sum: This popular problem is a great way to practice using hash tables for efficient search and retrieval.
# 242. Valid Anagram: This problem involves checking if two strings are anagrams, and hash tables are often used for this type of comparison.
# 49. Group Anagrams: A more advanced hash table problem where you need to group anagrams together.
# Sorting Algorithms

# Bubble Sort, Insertion Sort

# 912. Sort an Array: This problem explicitly asks you to sort an array, allowing you to practice implementing and comparing basic sorting algorithms like Bubble Sort and Insertion Sort.
# Merge Sort, Quick Sort

# Understand the underlying concepts: While LeetCode might not have direct problems requiring you to implement Merge Sort or Quick Sort from scratch, understanding their principles is crucial. Focus on grasping how they divide and conquer, the recursion involved, and their time complexities.
# Additional Tips

# Vary the difficulty: Start with easier problems to build confidence and gradually move towards more challenging ones.
# Read solutions and discussions: After solving a problem, read other solutions and participate in discussions to learn new techniques and approaches.
# Practice consistently: Set aside dedicated time each day or week to solve LeetCode problems and strengthen your algorithm skills.
# Remember, the key is to understand the core concepts of each algorithm, their strengths and weaknesses, and when to apply them effectively. By practicing these LeetCode problems and focusing on the underlying principles, 
# you'll be well-prepared for your technical interviews.



# Linear Search
# Linear search is a simple search algorithm that checks every element in the list until the target value is found or the list ends.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [4, 2, 3, 1, 5]
target = 3
result = linear_search(arr, target)
print(f"Linear Search Result: {result}")




# Binary seacrh 
# Binary search is an efficient algorithm for finding an item in a sorted list. It repeatedly divides the list in half and checks which half contains the target value.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
arr = [1, 2, 3, 4, 5]
target = 3
result = binary_search(arr, target)
print(f"Binary Search Result: {result}")

#  Bubble Sort
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
arr = [5, 1, 4, 2, 8]
sorted_arr = bubble_sort(arr)
print(f"Bubble Sort Result: {sorted_arr}")

# Selection Sort
# Selection sort is an algorithm that divides the list into two parts: a sorted and an unsorted sublist. It repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the sorted sublist.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(f"Selection Sort Result: {sorted_arr}")

# Merge Sort
# Merge sort is a divide-and-conquer algorithm that recursively splits the list into halves, sorts each half, and then merges them back together.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(f"Merge Sort Result: {sorted_arr}")



