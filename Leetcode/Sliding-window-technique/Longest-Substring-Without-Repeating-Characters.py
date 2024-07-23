# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


###################

# Intuition
# The intuition behind the 3 solutions is to iteratively find the longest substring without repeating characters by maintaining a sliding window approach. We use two pointers (left and right) to represent the boundaries of the current substring. As we iterate through the string, we update the pointers and adjust the window to accommodate new unique characters and eliminate repeating characters.

# Approach 2 - Unordered Map
# We improve upon the first solution by using an unordered map (charMap) instead of a set.
# The map stores characters as keys and their indices as values.
# We still maintain the left and right pointers and the maxLength variable.
# We iterate through the string using the right pointer.
# If the current character is not in the map or its index is less than left, it means it is a new unique character.
# 6 We update the charMap with the character's index and update the maxLength if necessary.
# If the character is repeating within the current substring, we move the left pointer to the next position after the last occurrence of the character.
# We update the index of the current character in the charMap and continue the iteration.
# At the end, we return the maxLength as the length of the longest substring without repeating characters.

##########################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLength

######## Line-by-Line Explanation ########

# Class Definition:
class Solution:


# Defines a class named Solution.
# Method Definition:
def lengthOfLongestSubstring(self, s: str) -> int:


# Defines a method lengthOfLongestSubstring that takes a string s as input and returns an integer.
# Initialize Variables:
n = len(s)
maxLength = 0
charMap = {}
left = 0


# n stores the length of the string s.
# maxLength initializes the maximum length of the substring without repeating characters to 0.
# charMap is an empty dictionary to keep track of the last index of each character.
# left is initialized to 0, representing the start index of the sliding window.
# Iterate Over the String:
for right in range(n):

# Starts a loop from 0 to n-1, with right as the loop variable. This represents the end index of the sliding window.
# Check for Repeating Characters:
if s[right] not in charMap or charMap[s[right]] < left:

# Checks if the character at index right is not in charMap or its last recorded index is less than left. This means the character is either not seen before or it’s outside the current window.
# Update Character Map and Max Length:
charMap[s[right]] = right
maxLength = max(maxLength, right - left + 1)

# Updates charMap with the current character’s index right.
# Calculates the current window’s length (right - left + 1) and updates maxLength with the maximum value between the current maxLength and the new length.
# Adjust Left Pointer if a Repetition is Found:
else:
    left = charMap[s[right]] + 1
    charMap[s[right]] = right

# If the character at right is already in charMap and its last index is within the current window (charMap[s[right]] >= left), update left to charMap[s[right]] + 1 to exclude the repeated character from the window.
# Update the character’s index in charMap to right.
# Return the Result:
return maxLength

# Returns the maximum length of the substring without repeating characters.


# Summary
# Approach: This algorithm uses the sliding window technique with two pointers (left and right) to efficiently find the longest substring without repeating characters. The charMap dictionary helps in tracking the latest index of each character.
# Time Complexity: 
# 𝑂(𝑛)
# O(n), where 
# 𝑛
# n is the length of the string. Each character is processed once, making the solution linear in time complexity.
# Space Complexity: 
# 𝑂(𝑚𝑖𝑛(𝑛,𝑚))
# O(min(n,m)), where 𝑚
# m is the size of the character set. The charMap stores the indices of characters and thus uses space proportional to the size of the character set.
