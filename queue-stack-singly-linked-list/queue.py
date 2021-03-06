from singly_linked_list import LinkedList
from stack import Stack
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# with array
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1
        return self

    def dequeue(self):
        if len(self) > 0:
            first = self.storage.pop(0)
            self.size -= 1
            return first
        else:
            return None
"""

# with LinkedList

"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        return self

    def dequeue(self):
        if len(self) > 0:
            first = self.storage.remove_head()
            self.size -= 1
            return first
        else:
            return None
"""


class Queue:
    def __init__(self):
        self.incoming = []
        self.outgoing = []

    def __len__(self):
        return len(self.incoming) + len(self.outgoing)

    def enqueue(self, item):
        self.incoming.append(item)

    def dequeue(self):
        if self.outgoing:
            return self.outgoing.pop()

        while self.incoming:
            item = self.incoming.pop()
            self.outgoing.append(item)

        return self.outgoing.pop()


q = Queue()
for i in range(10):
    q.enqueue(i)
    print("i:", i)
for i in range(10):
    print(q.dequeue()),
