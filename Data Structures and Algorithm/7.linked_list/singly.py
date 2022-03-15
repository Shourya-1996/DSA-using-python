class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


singly = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singly.head = node1
singly.head.next = node2
singly.tail = node2
