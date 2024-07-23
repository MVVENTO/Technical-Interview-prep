# What is a Linked List?
# A linked list is a linear data structure where elements are stored in nodes. Each node contains:

# Data: The value or data of the node.
# Next Pointer: A reference to the next node in the sequence.
# Types of Linked Lists
# Singly Linked List: Each node points to the next node and the last node points to None.
# Doubly Linked List: Each node has two pointers, one to the next node and one to the previous node.
# Circular Linked List: The last node points back to the first node, forming a circle.


# Implementing a Singly Linked List
# Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


# Key Operations
# Insertion at the Beginning
def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


# Insertion at the End.
def append(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    last = self.head
    while last.next:
        last = last.next
    last.next = new_node


# Deletion of a Node
def delete_with_value(self, key):
    temp = self.head
    if temp and temp.data == key:
        self.head = temp.next
        temp = None
        return
    while temp and temp.next:
        if temp.next.data == key:
            temp.next = temp.next.next
            return
        temp = temp.next


# Display Linked List
def display(self):
    elements = []
    current = self.head
    while current:
        elements.append(current.data)
        current = current.next
    return elements



# Implementing a Doubly Linked List


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_with_value(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                temp = None
                return
            temp = temp.next

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display_backward(self):
        elements = []
        last = self.head
        while last and last.next:
            last = last.next
        while last:
            elements.append(last.data)
            last = last.prev
        return elements




# Common Operations and Algorithms
# Detecting a Cycle

# Use Floyd’s Cycle-Finding Algorithm (Tortoise and Hare):
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Finding the Middle Node
# Use two pointers, one moving twice as fast as the other:
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Reversing a Linked List
# Iteratively or recursively:

def reverse_iteratively(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head




# Practical Tips
# Initialization: Always initialize the head to None for an empty list.
# Edge Cases: Handle cases where the list is empty or has only one element.
# Memory Management: In Python, garbage collection handles memory management, but ensure you break references to nodes when deleting.
# Practice Problems
# Reverse a Linked List
# Detect a Cycle
# Find the Intersection Point of Two Linked Lists
# Merge Two Sorted Linked Lists
# Remove N-th Node from End of List

#EXAMPLE

# Singly Linked List Example
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
print(linked_list.display())  # Output: [0, 1, 2, 3]
linked_list.delete_with_value(2)
print(linked_list.display())  # Output: [0, 1, 3]

# Doubly Linked List Example
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.prepend(0)
print(dll.display_forward())  # Output: [0, 1, 2]
print(dll.display_backward()) # Output: [2, 1, 0]
dll.delete_with_value(1)
print(dll.display_forward())  # Output: [0, 2]



##########################################################

# To connect and utilize the Node and DoublyLinkedList classes you’ve provided, let’s walk through the complete implementation with explanations.
#  Here’s the complete code, including class definitions and some example usage to demonstrate how to create, manipulate, and display a doubly linked list:

# Node Class Definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List Class Definition
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a new node with the specified data to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        """
        Prepend a new node with the specified data to the start of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_with_value(self, key):
        """
        Delete the first node with the specified value from the list.
        """
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                temp = None
                return
            temp = temp.next

    def display_forward(self):
        """
        Display all elements in the list from head to tail.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display_backward(self):
        """
        Display all elements in the list from tail to head.
        """
        elements = []
        last = self.head
        while last and last.next:
            last = last.next
        while last:
            elements.append(last.data)
            last = last.prev
        return elements

# Example Usage
if __name__ == "__main__":
    # Create a doubly linked list
    dll = DoublyLinkedList()

    # Append elements
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    print("List after appending elements:", dll.display_forward())  # Output: [1, 2, 3, 4]

    # Prepend elements
    dll.prepend(0)
    print("List after prepending an element:", dll.display_forward())  # Output: [0, 1, 2, 3, 4]

    # Delete an element
    dll.delete_with_value(2)
    print("List after deleting element with value 2:", dll.display_forward())  # Output: [0, 1, 3, 4]

    # Display list forward and backward
    print("List displayed forward:", dll.display_forward())  # Output: [0, 1, 3, 4]
    print("List displayed backward:", dll.display_backward())  # Output: [4, 3, 1, 0]
# Explanation of Code
# Node Class:

# The Node class initializes each node with data, next, and prev attributes.
# DoublyLinkedList Class:

# The __init__ method initializes an empty list.
# append(data): Adds a node with the specified data to the end of the list.
# prepend(data): Adds a node with the specified data to the beginning of the list.
# delete_with_value(key): Removes the first node containing the specified data.
# display_forward(): Returns a list of all elements from head to tail.
# display_backward(): Returns a list of all elements from tail to head.
# Example Usage: Demonstrates how to create a doubly linked list, append and prepend nodes, delete a node, and display the list both forward and backward.

