# Checking for Palindrome 

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Line-by-Line Breakdown



# Function Definition:
def is_palindrome(s):
# Defines a function named is_palindrome that takes one argument s, which is the string to be checked.


# Initialize Pointers:
left, right = 0, len(s) - 1
# left is initialized to 0, pointing to the start of the string.
# right is initialized to len(s) - 1, pointing to the end of the string.

# While Loop:
while left < right:
# The loop continues as long as left is less than right. This ensures that we only check up to the middle of the string.
  
# Check Characters:
if s[left] != s[right]:
    return False
# Compares the characters at the left and right pointers.
# If the characters are not equal (s[left] != s[right]), the string is not a palindrome, so the function immediately returns False.

# Move Pointers:
left += 1
right -= 1
# Moves the left pointer one step to the right (left += 1).
# Moves the right pointer one step to the left (right -= 1).
# This step moves the pointers towards the center of the string, allowing for the next comparison.

# Return True:
return True
# If the loop completes without finding any mismatched characters, the string is a palindrome. The function returns True.
