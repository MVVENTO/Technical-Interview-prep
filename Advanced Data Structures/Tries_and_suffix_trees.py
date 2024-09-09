# Tries (Prefix Trees)
# Key Concepts of Tries:
# Trie (Prefix Tree) is a tree-like data structure used to efficiently store and search strings by breaking them down character by character.
# Each node represents a single character.
# The root node is empty, and each path from the root to a leaf node represents a word or prefix.
# Trie Operations:
# Inserting a Word:

# Traverse the trie from the root, for each character in the word:
# If the character doesn't exist as a child node, create a new node.
# Move to the child node.
# Mark the end of the word at the last node.
# Time complexity: O(m) (where m is the length of the word).
# Searching a Word:

# Traverse the trie based on the characters of the input word.
# If all characters match and the last node is marked as the end of a word, return True.
# Time complexity: O(m).
# Prefix Search (Autocomplete):

# Traverse the trie for the given prefix.
# If the prefix is found, collect all words starting with that prefix by performing a depth-first search (DFS) from the current node.
# Time complexity: O(m + k), where k is the number of words with the given prefix.
# Deleting a Word:

# Traverse to the end of the word, then backtrack to remove nodes that are no longer part of another word.
# Time complexity: O(m).
# Trie Implementation in Python:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Search for a word in the Trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # Check if a prefix exists in the Trie
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    # Autocomplete: Find all words with the given prefix
    def autocomplete(self, prefix):
        def dfs(node, prefix):
            results = []
            if node.is_end_of_word:
                results.append(prefix)
            for char, next_node in node.children.items():
                results += dfs(next_node, prefix + char)
            return results

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return dfs(node, prefix)

# Usage Example:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
print(trie.search("app"))  # True
print(trie.search("bat"))  # False
print(trie.autocomplete("ap"))  # ['apple', 'app']



# Applications of Tries:
# Autocomplete: Efficiently find words that match a given prefix.
# Spell Checking: Identify valid words and suggest corrections.
# IP Routing: Store IP prefixes for network routing.
# Dictionary Matching: Search for patterns in texts.
# Longest Prefix Matching: Used in text editors and web search engines.
# 2. Suffix Trees
# Key Concepts of Suffix Trees:
# Suffix Tree is a compressed trie of all suffixes of a given string.
# Efficient for solving complex string matching problems, such as finding the longest common substring, substring search, and pattern matching.
# Suffix Trees reduce the complexity of many string operations from O(n^2) to O(n) or O(m) (where n is the length of the text and m is the length of the pattern).
# Operations with Suffix Trees:
# Constructing a Suffix Tree:

# Build a tree where each suffix of a string is represented as a path from the root to a leaf node.
# Time complexity: O(n) using Ukkonen's algorithm (for optimized suffix tree construction).
# Substring Search:

# Given a pattern, traverse the tree to match characters of the pattern.
# If all characters match, the pattern exists in the string.
# Time complexity: O(m) (where m is the length of the pattern).
# Longest Common Substring:

# Given two strings, build a suffix tree for the concatenation of both strings.
# Traverse the tree and find the deepest node that corresponds to substrings of both strings.
# Time complexity: O(n).
# Naive Suffix Tree Implementation in Python:
# Suffix trees are more complex than tries, and building them efficiently typically requires Ukkonen's algorithm. Below is a basic naive implementation to demonstrate the concept.


class SuffixTreeNode:
    def __init__(self):
        self.children = {}

class SuffixTree:
    def __init__(self):
        self.root = SuffixTreeNode()

    # Build the suffix tree for the given text
    def build_suffix_tree(self, text):
        for i in range(len(text)):
            current_node = self.root
            suffix = text[i:]
            for char in suffix:
                if char not in current_node.children:
                    current_node.children[char] = SuffixTreeNode()
                current_node = current_node.children[char]

    # Check if a pattern exists in the text using the suffix tree
    def search(self, pattern):
        current_node = self.root
        for char in pattern:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Usage Example:
stree = SuffixTree()
stree.build_suffix_tree("banana")
print(stree.search("ana"))  # True
print(stree.search("nan"))  # True
print(stree.search("band"))  # False


# Suffix Tree Applications:
# Pattern Matching: Efficiently check if a pattern exists in a text.
# Finding Repeated Substrings: Detect the longest repeated substring in a text.
# Longest Common Substring: Identify the longest shared substring between two or more strings.
# Genome Sequencing: Used in bioinformatics for DNA sequence alignment and comparison.
# Key Considerations for Google Interviews:
# Suffix Arrays: Consider also learning suffix arrays, which are space-efficient alternatives to suffix trees but achieve similar tasks.
# Optimized Construction: Understand Ukkonen’s algorithm for linear-time suffix tree construction.
# Practice Problems:
# Implement Trie (Prefix Tree)

# LeetCode #208
# Difficulty: Medium
# Add and Search Word - Data Structure Design

# LeetCode #211
# Difficulty: Medium
# Word Search II

# LeetCode #212
# Difficulty: Hard
# Longest Common Substring

# Description: Implement using suffix trees/arrays.
# Difficulty: Medium/Hard
# Longest Repeated Substring

# Description: Find the longest repeated substring using suffix trees.
# Difficulty: Hard
# By mastering Tries and Suffix Trees and practicing the related problems, you'll be well-prepared to tackle string-related challenges in a Google technical interview!


