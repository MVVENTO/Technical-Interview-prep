# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution:
    def maxArea(self, height):
        left = 0            # Left pointer starting from the leftmost edge
        right = len(height) - 1  # Right pointer starting from the rightmost edge
        maxWater = 0        # Initialize the maximum water capacity
        
        while left < right:
            # Calculate the width of the container
            width = right - left
            
            # Calculate the height of the container (the minimum height between the two lines)
            h = min(height[left], height[right])
            
            # Calculate the water capacity of the current container
            water = width * h
            
            # Update the maximum water capacity if the current container holds more water
            maxWater = max(maxWater, water)
            
            # Move the pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater
      
# Line-by-Line Explanation
# Class Definition:
class Solution:


# Defines a class named Solution which contains the method maxArea.
# Method Definition:
def maxArea(self, height):


# Defines a method maxArea that takes one parameter height, which is a list of integers representing the heights of lines.
# Initialize Pointers and Variables:.
left = 0            # Left pointer starting from the leftmost edge
right = len(height) - 1  # Right pointer starting from the rightmost edge
maxWater = 0        # Initialize the maximum water capacity


# left pointer is initialized at 0, the start of the array.
# right pointer is initialized at len(height) - 1, the end of the array.
# maxWater is initialized to 0 to keep track of the maximum water capacity found.
# Start of While Loop:
while left < right:


# The loop runs as long as left is less than right, ensuring that the pointers do not cross each other.
# Calculate Width of Container:
width = right - left


# Computes the width of the container formed by the lines at left and right.
# Calculate Minimum Height:
h = min(height[left], height[right])

# Determines the height of the container as the minimum height between height[left] and height[right].
# Calculate Water Capacity:
water = width * h


# Calculates the area (water capacity) of the current container using the formula width * height.
# Update Maximum Water Capacity:
maxWater = max(maxWater, water)


# Updates maxWater to be the maximum of its current value and water.
# Move the Pointers:
if height[left] < height[right]:
    left += 1
else:
    right -= 1


# If the height at left is less than the height at right, increment left to potentially find a taller line.
# Otherwise, decrement right to potentially find a taller line.
# Return the Result:
return maxWater


#   Approach: The two-pointer technique is used to find the maximum area efficiently. The pointers start at the ends of the array and move towards each other based on the height comparison.
# Time Complexity: 
# 𝑂(𝑛)
# O(n), where 𝑛n is the number of lines in the height array. This is because each pointer moves at most once through the list.
# Space Complexity: 
# 𝑂(1)
# O(1), as only a few variables are used, regardless of the input size.



