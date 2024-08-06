# Stacks
# Definition
# A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
# The most recently added element is the one that is removed first.

# Operations
#   Push: Add an element to the top of the stack.
#   Pop: Remove and return the top element of the stack.
#   Peek/Top: Return the top element without removing it.
#   IsEmpty: Check if the stack is empty.

# Implementation
#   Array-Based Stack:
#   Use an array to store elements.
#   Keep an index to track the top of the stack.

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
        
    def is_empty(self):
        return len(self.stack) == 0


# Linked List-Based Stack:
# Use a linked list to store elements.
# The head of the list represents the top of the stack.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.value
            self.top = self.top.next
            return popped_item
        return None

    def peek(self):
        if not self.is_empty():
            return self.top.value
        return None

    def is_empty(self):
        return self.top is None

# Common Interview Problems
# Balanced Parentheses: Check if an expression has balanced parentheses.

# Min Stack: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Evaluate Postfix Expression: Evaluate a given postfix expression.



# Queues
# Definition
# A queue is a linear data structure that follows the First In First Out (FIFO) principle.
# The first element added is the first one to be removed.
# Operations

#    Enqueue: Add an element to the end of the queue.
#   Dequeue: Remove and return the front element of the queue.
#   Peek/Front: Return the front element without removing it.
#   IsEmpty: Check if the queue is empty.

# Implementation
#   Array-Based Queue:
#       Use an array to store elements.
#       Maintain indices for the front and rear of the queue.


class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None
        
    def is_empty(self):
        return len(self.queue) == 0


# Linked List-Based Queue:
# Use a linked list to store elements.
# Maintain pointers to the front and rear of the queue.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = self.rear

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.front.value
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return dequeued_item
        return None

    def peek(self):
        if not self.is_empty():
            return self.front.value
        return None

    def is_empty(self):
        return self.front is None

# Common Interview Problems
# Implement a Stack Using Queues: Use two queues to implement a stack.
# First Unique Character in a String: Use a queue to find the first non-repeating character in a stream of characters.
# Circular Queue: Implement a circular queue with a fixed size.
# Cracking the Coding Interview: Specific Problems
# Problem 1: Three in One (Stacks)
# Problem: Describe how you could use a single array to implement three stacks.
# Solution:
# Divide the array into three equal parts and allocate each part to a stack.
# Use additional arrays to keep track of the tops of each stack.

class ThreeInOne:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_capacity = stack_size
        self.values = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise Exception("Stack is full")
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]
        self.values[top_index] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        return self.values[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_capacity

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_capacity
        return offset + self.sizes[stack_num] - 1


# Problem 2: Stack Min (Stacks)
# Problem: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.
# Solution:
# Use an auxiliary stack to keep track of the minimum values.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if value == self.min_stack[-1]:
                self.min_stack.pop()
            return value
        return None

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None


# Problem 3: Animal Shelter (Queues)
# Problem: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether 
# they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like.
#  Create the data structures to maintain this system and implement operations such as enqueue, dequeue_any, dequeue_dog, and dequeue_cat.

class Animal:
    def __init__(self, name):
        self.name = name
        self.order = None

    def set_order(self, order):
        self.order = order

    def get_order(self):
        return self.order

    def is_older_than(self, other):
        return self.order < other.get_order()

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, animal):
        animal.set_order(self.order)
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeue_any(self):
        if not self.dogs:
            return self.dequeue_cat()
        if not self.cats:
            return self.dequeue_dog()
        dog = self.dogs[0]
        cat = self.cats[0]
        if dog.is_older_than(cat):
            return self.dequeue_dog()
        else:
            return


