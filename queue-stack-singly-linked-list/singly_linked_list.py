class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"<Node value: {self.value} at {hex(id(self))}>"


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_tail(self):
        if self.head is None:
            return

        if self.head is self.tail:
            return self.remove_head()

        curr = self.head
        while curr.next_node is not self.tail:
            curr = curr.next_node

        old_tail = curr.next_node
        self.tail = curr
        self.tail.next_node = None
        return old_tail.value

    def remove_head(self):
        # empty LL
        if self.head is None:
            return None

        # LL with one Node
        if self.head.next_node is None:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.value

        old_head = self.head
        self.head = self.head.next_node
        return old_head.value

    def contains(self, value):
        if self.head is None:
            return False

        curr = self.head
        while True:
            if curr.value == value:
                return True
            if curr is self.tail:
                return False
            curr = curr.next_node

    def get_max(self):
        if not self.head:
            return None

        curr = self.head
        max_value = curr.value

        while curr:
            if curr.value > max_value:
                max_value = curr.value
            curr = curr.next_node

        return max_value


ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
