# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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
    
    def __str__(self):
        if not self.head:
            return "empty"
        current = self.head
        result = []
        while current:
            result.append(f"[{current.data}|•]")
            current = current.next
        result.append("null")
        return " -> ".join(result)

sll = SinglyLinkedList()
sll.append(3)
sll.append(7)
sll.append(1)
sll.append(9)
sll.append(4)
print("Singly Linked List:", sll)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

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

    def __str__(self):
        if not self.head:
            return "empty"
        current = self.head
        result = ["null"]
        while current:
            result.append(f"[{current.data}|•|•]")
            current = current.next
        result.append("null")
        return " <-> ".join(result)


dll = DoublyLinkedList()
dll.append(3)
dll.append(7)
dll.append(1)
dll.append(9)
dll.append(4)
print("Doubly Linked List:", dll)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head

# Usage
cll = CircularLinkedList()
cll.append(3)
cll.append(7)
cll.append(1)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
