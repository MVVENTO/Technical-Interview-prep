# What is a singly linked list?

# Singly Linked List is a collection of nodes that form a linear sequence
# Each node stores a reference to the next node
# The first and last node of the list are known as the "head" and the "tail" of the list
# Process of moving through the list is "traversing"
# Each node stores a reference to the element and the next node (except the tail)
# How do we add a new element?
# Example to append to the Head (inverse can be done for appending to the Tail) - We create a new node - Set its element to the new element - Set the next link to refer to the current head - Set the list's head to point to the new node
# Removing an element from the Head is essentially the reverse operation to adding the item
# We cannot easily remove the last node - to do so efficiently requires a doubly linked list
# O(k) time to access elements
# Constant time insertions and deletions in any position, arrays require O(n) time
# Linked Lists can expand without having to specify their size ahead of time!

class Node(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)

# how to link the nodes?
a.nextNode = b
b.nextNode = c

# What is a doubly linked list?

# next and prev for references to nodes that are both next and what precedes it
# "dummy" nodes are known as the header sentinel and trailer sentinel for both the beginning and end of a list respectively
# Each insertion happens between a pair of existing nodes - eg. Add between header and what is after to add to the front

class Node(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None
		self.prevNode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.prevNode = a
b.nextNode = c
c.prevNode = b


# For a Google technical interview, you'll want to be well-prepared with a variety of Linked List problems. Here are some common LeetCode problems that are frequently asked in interviews and cover a range of linked list concepts:

# 1. Basic Linked List Operations
# Reverse Linked List

# Description: Reverse a singly linked list.
# Skills: Understanding of linked list traversal and modification.
# Merge Two Sorted Lists

# Description: Merge two sorted linked lists into one sorted linked list.
# Skills: Merging lists while maintaining order.
# Linked List Cycle

# Description: Determine if a linked list has a cycle.
# Skills: Detecting cycles using fast and slow pointers (Floyd’s Tortoise and Hare algorithm).
# 2. Intermediate Problems
# Add Two Numbers

# Description: Add two numbers represented by linked lists.
# Skills: Handling addition with carry-over.
# Remove Nth Node From End of List

# Description: Remove the N-th node from the end of the list.
# Skills: Two-pass or one-pass techniques with two pointers.
# Intersection of Two Linked Lists

# Description: Find the node where two linked lists intersect.
# Skills: Using pointer manipulation to find intersection.
# 3. Advanced Problems
# Copy List with Random Pointer

# Description: Copy a list where each node has a random pointer.
# Skills: Deep copying nodes with multiple pointers (next and random).
# Rearrange Linked List

# Description: Rearrange nodes in a linked list.
# Skills: In-place reordering and manipulation of nodes.
# Sort List

# Description: Sort a linked list using merge sort.
# Skills: Efficient sorting algorithm implementation for linked lists.
# 4. Extra Practice
# Partition List

# Description: Partition a linked list around a value x, such that all nodes less than x come before nodes greater than or equal to x.
# Skills: Partitioning and reorganizing nodes.
# Rotate List

# Description: Rotate a linked list to the right by k places.
# Skills: Rotation and handling of circular linked lists.
# Linked List Cycle II

# Description: Find the node where the cycle begins in a linked list.
# Skills: Cycle detection and finding the start of the cycle.
# Tips for Solving Linked List Problems
# Understand the Problem: Clearly identify whether it’s a singly or doubly linked list and if any special pointers (like random pointers) are involved.
# Practice Edge Cases: Handle cases like empty lists, single-node lists, and lists with only two nodes.
# Optimize Space and Time: Aim for efficient solutions in terms of both time and space complexity, especially for large inputs.
# Draw Diagrams: Visualize the linked list and operations to understand the changes happening to nodes and pointers.


# 3. Linked Lists
# Reverse Linked List

# Description: Reverse a singly linked list.
# Skills: Linked list traversal and modification.
# Merge Two Sorted Lists

# Description: Merge two sorted linked lists into one sorted list.
# Skills: Merging lists.
# Add Two Numbers

# Description: Add two numbers represented by linked lists.
# Skills: Carry-over addition.
# Linked List Cycle

# Description: Determine if a linked list has a cycle.
# Skills: Cycle detection (Floyd’s Tortoise and Hare).
