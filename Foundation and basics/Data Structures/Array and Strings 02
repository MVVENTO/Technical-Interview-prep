############## ARRAY ###############
#Definition: An array is a collection of items stored at contiguous memory locations. In Python, lists are used to implement arrays.

arr = [1, 2, 3, 4, 5]

# 2: Operations 

# Accessing Elements: Use index notation.
print(arr[0])  # Output: 1

#Slicing: Extract a subset of elements
sub_arr = arr[1:4]  # [2, 3, 4]

#Appending: Add an element to the end
arr.append(6)

#Inserting: Insert an element at a specific index.
arr.insert(2, 10)  # [1, 2, 10, 3, 4, 5, 6]

#Removing: Remove an element by value or index.
arr.remove(10)  # [1, 2, 3, 4, 5, 6]
arr.pop(2)      # [1, 2, 4, 5, 6]

#Length: Get the number of elements.
len(arr)  # 5

# 3: Common Problems

#Two Sum: Find two numbers that add up to a target.
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i


#Rotate Array: Rotate elements k steps to the right.
def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]


########## STRING #############

# Definition: A string is a sequence of characters.

s = "hello"


# 2. String Operations

#Concatenation: Join strings.
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2  # "Hello World"


#Slicing: Extract a substring.
substr = s[1:4]  # "ell"


# Length: Get the length of the string.
len(s)  # 5


#String Methods:

# Upper/Lower Case:
s.upper()  # "HELLO"
s.lower()  # "hello"


# Strip Whitespace:
s.strip()  # Removes leading/trailing whitespace


# Replace
s.replace("hello", "hi")  # "hi"


# Split:
s.split()  # ['hello']



#Slicing: Extract a substring.
substr = s[1:4]  # "ell"


# Length: Get the length of the string.
len(s)  # 5


#String Methods:

# Upper/Lower Case:
s.upper()  # "HELLO"
s.lower()  # "hello"


# Strip Whitespace:
s.strip()  # Removes leading/trailing whitespace


# Replace
s.replace("hello", "hi")  # "hi"


# Split:
s.split()  # ['hello']

#string indexing

s = "Hello World"

# Indexing
# show first element 
s[0]

s[1]

s[2]

# slicing
# Grab everything past the first term all the way to the Length of s which is len(s) 
s[1:]

# grab everything UP TO the 3rd index
s[:3]

# Everything
s[:]

# Last letter 
s[-1]

# grab everything but the last letter
s[:-1]

# Grab everything, but go in steps size of 1
s[::1]

# Grab everything but go in step sizes of 2
s[::2]

# we can use this to print a string backwards
s[::-1]


# 3. Common Problems

# Reverse a String:
def reverse_string(s):
    return s[::-1]


# Check Palindrome:
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


# 4. Algorithmic Problems

# Longest Substring Without Repeating Characters:
def length_of_longest_substring(s):
    chars = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in chars:
            left = max(left, chars[s[right]] + 1)
        chars[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length


# Valid Anagram:

def is_anagram(s, t):
    return sorted(s) == sorted(t)




# Tips for Google Interviews

# Understand the Problem Statement: Clarify any ambiguities before you start coding.
# Write Clean Code: Use meaningful variable names and comments.
# Edge Cases: Consider edge cases like empty inputs, single-element arrays, or strings with special characters.
# Optimize: Think about time and space complexity. Aim for O(n) or O(n log n) solutions where possible.
# Practice: Use platforms like LeetCode, HackerRank, or CodeSignal to practice.

# Recommended Practice Problems

# Arrays:
# Two Sum       :       https://leetcode.com/problems/two-sum/description/
# Best Time to Buy and Sell Stock       : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Product of Array Except Self           : https://leetcode.com/problems/product-of-array-except-self/description/

# Strings:
# Longest Substring Without Repeating Characters       : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Valid Palindrome       : https://leetcode.com/problems/valid-palindrome/description/
# Longest Common Prefix        : https://leetcode.com/problems/longest-common-prefix/description/



###################################  NOTES ################################
# The for Loop
# python
# Copy code
# for i in range(n - 2, -1, -1):
# This loop iterates over the indices of an array in reverse order. Here’s a step-by-step explanation:

# range(start, stop, step) is a built-in Python function that generates a sequence of numbers.
# start: The starting point of the sequence.
# stop: The point where the sequence stops (not inclusive).
# step: The step or increment between each number in the sequence.
# In this specific loop:

# start is n - 2. This means the loop starts at the second-to-last element of the array.
# stop is -1. This means the loop will stop before reaching -1, effectively stopping at 0.
# step is -1. This means the loop will decrement by 1 in each iteration, moving backwards through the array.
