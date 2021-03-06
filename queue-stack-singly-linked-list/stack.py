from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# Using array

"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        return self

    def pop(self):
        if (len(self.storage) > 0):
            popped = self.storage.pop()
            return popped
"""

# Using LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        return self

    def pop(self):
        if(len(self) > 0):
            popped = self.storage.remove_tail()
            self.size -= 1
            return popped
        else:
            return None


stack = Stack()
stack.push(100)
stack.push(101)
stack.push(105)
