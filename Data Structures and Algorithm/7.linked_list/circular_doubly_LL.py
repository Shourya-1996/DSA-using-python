class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def CreateCDLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        return "list is created"

    def insertNode(self, value, location):
        if self.head is None:
            print("list does not exist")
        else:
            newNode = Node(value)
            if location == 0:
                # at the beginning of the list
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                # at the end of the list
                newNode.prev = self.tail
                newNode.next = self.head
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location-1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                newNode.next = nextNode
                newNode.prev = currentNode
                currentNode.next = newNode
                nextNode.prev = newNode
            return "the node has been successfully inserted"

    def traverseCDLL(self):
        if self.head is None:
            return "list does not exist"
        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.next
                if currentNode == self.head:
                    break

    def reversetraverseCDLL(self):
        if self.head is None:
            return "list does not exist"
        else:
            currentNode = self.tail
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.prev
                if currentNode == self.head.prev:
                    break

    def searchCDLL(self, value):
        if self.head is None:
            return "list does not exist"
        else:
            currentNode = self.head
            while currentNode:
                if currentNode.value == value:
                    print("value exist in the list")
                    break
                currentNode = currentNode.next
                if currentNode == self.head:
                    print("value does not exist")
                    break

    def deleteNode(self, location):
        if self.head is None:
            return "list does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currentNode = self.head
                index = 0
                while index < location-1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next
                nextNode.prev = currentNode
            print("node is deleted successfully")

    def deleteEntireCDLL(self):
        if self.head is None:
            return "list does not exist"
        else:
            currentNode = self.head
            while currentNode != self.head:
                currentNode.prev = None
                currentNode = currentNode.next
            self.head = None
            self.tail = None
            print("the CDLL has been successfully deleted")


cdll = CircularDoublyLL()

print(cdll.CreateCDLL(1))
print([node.value for node in cdll])
cdll.insertNode(0, 0)
cdll.insertNode(2, 1)
cdll.insertNode(20, 0)
cdll.insertNode(30, 1)
cdll.insertNode(40, 2)
print([node.value for node in cdll])
# cdll.traverseCDLL()
# cdll.reversetraverseCDLL()
# cdll.searchCDLL(20)
cdll.deleteNode(3)
print([node.value for node in cdll])
cdll.deleteEntireCDLL()
print([node.value for node in cdll])
