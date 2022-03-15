class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
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
    # creating Circular linked list

    def createCSLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return "Circular Singly Linked List is created"

    # inserting an element in CSLL

    def insertCSLL(self, value, location):
        if self.head is None:
            return "The List does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "Node has been inserted"

    def travereCSLL(self):
        if self.head is None:
            return "list does not exist"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchElement(self, value):
        if self.head == None:
            return "list does not exist"
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                if tempNode.value == value:
                    print(f"Element exist in this list at index {index}")
                tempNode = tempNode.next
                index += 1
                if tempNode == self.tail.next:
                    print("element does not exist")
                    break

    def deleteNode(self, location):
        if self.head == None:
            return "List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    currentNode = self.head
                    while currentNode.next != self.tail:
                        currentNode = currentNode.next
                    currentNode.next = self.head
                    self.tail = currentNode

            else:
                currentNode = self.head
                index = 0
                while index < location-1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next
                return "node deleted"

    def deleteEntireCSLL(self):
        self.tail.next = None
        self.head = None
        self.tail = None


circularSLL = CircularSinglyLinkedList()
print(list(node.value for node in circularSLL))
circularSLL.createCSLL(1)
print(list(node.value for node in circularSLL))
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(3, 1)
circularSLL.insertCSLL(4, 2)
circularSLL.insertCSLL(4, 1)
circularSLL.insertCSLL(5, 1)
print([node.value for node in circularSLL])
circularSLL.deleteNode(3)
circularSLL.deleteEntireCSLL()
print([node.value for node in circularSLL])
# circularSLL.travereCSLL()
# circularSLL.searchElement(40)
