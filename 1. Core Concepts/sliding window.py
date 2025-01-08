# The sliding window technique is used to reduce time complexity in array or string problems. It involves keeping a window of a fixed size and sliding it across the data.

# 🔧 Example: Longest Substring Without Repeating Characters

def length_of_longest_substring(s):
    char_set = set()
    l = 0
    max_length = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        max_length = max(max_length, r - l + 1)

    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # Output: 3
