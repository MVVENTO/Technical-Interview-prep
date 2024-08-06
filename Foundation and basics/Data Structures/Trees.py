# 1. Binary Trees
# Definition:

# A Binary Tree is a tree data structure where each node has at most two children, commonly referred to as the left child and the right child.
# Properties:

# Height: The length of the longest path from the root to a leaf.
# Depth: The length of the path from the root to a node.
# Complete Binary Tree: All levels, except possibly the last, are completely filled, and all nodes are as far left as possible.
# Full Binary Tree: Every node other than the leaves has exactly two children.
# Common Operations:

# Traversal: Visiting all nodes in a specific order. Common traversals include:
# In-order (Left, Root, Right)
# Pre-order (Root, Left, Right)
# Post-order (Left, Right, Root)
# Level-order (Breadth-First)

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

      
# 2. Binary Search Trees (BST)
# Definition:

# A Binary Search Tree is a Binary Tree where the left child of a node contains only nodes with values less than the node’s value, and the right child only nodes with values greater.
# Properties:

# In-order Traversal: Produces a sorted list of values.
# Searching: Efficiently done in O(log n) time complexity on average.
# Common Operations:

# Insertion: Add a value while maintaining the BST property.
# Deletion: Remove a node while preserving the BST property.
# Search: Find a node with a specific value.
# Find Minimum/Maximum: Find the smallest or largest value in the BST.


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

# 3. AVL Trees
# Definition:

# An AVL Tree is a self-balancing Binary Search Tree where the difference between heights of left and right subtrees cannot be more than one for any node.
# Properties:

# Balance Factor: The height difference between left and right subtrees. It must be -1, 0, or 1.
# Rotations:

# Right Rotation
# Left Rotation
# Right-Left Rotation
# Left-Right Rotation
# Common Operations:

# Insertion: Includes rotations to maintain balance.
# Deletion: Similar to insertion, it may require rotations to maintain balance.


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(root, value):
    if not root:
        return TreeNode(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1 and value < root.left.value:
        return right_rotate(root)
    if balance < -1 and value > root.right.value:
        return left_rotate(root)
    if balance > 1 and value > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and value < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
