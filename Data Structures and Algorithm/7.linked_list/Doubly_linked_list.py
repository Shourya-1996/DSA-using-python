class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init_(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # creat doubly linked list
    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "Doubly Linked List is created"

    def insertNode(self, value, location):
        if self.head is None:
            return "List does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location-1:
                    currentNode = currentNode.next
                    index += 1
                newNode.prev = currentNode
                newNode.next = currentNode.next
                newNode.next.prev = newNode
                currentNode.next = newNode
            return "Node added to the list"

    def forwardtraverseDLL(self):
        if self.head == None:
            return "list does not exist"
        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.next

    def reversetraverseDLL(self):
        if self.head == None:
            return "list does not exist"
        else:
            currentNode = self.tail
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.prev

    def searchElementDLL(self, value):
        if self.head == None:
            return "list does not exist "
        else:
            currentNode = self.head
            while currentNode:
                if currentNode.value == value:
                    # print("List contains this element")
                    return "List contains this element"
                currentNode = currentNode.next
            return "element does not exist"

    def deleteElement(self, location):
        if self.head == None:
            return "list does not exist "
        else:
            # deleting 1st element
            if location == 0:
                # if list contain only 1 element
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    # if list contains more than 1 element
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                # deleting last element
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next
                nextNode.prev = currentNode
            print("node successfully delelted")

    def deleteEntireDLL(self):
        if self.head is None:
            print("list does not exist")
        else:
            currentNode = self.head
            while currentNode:
                currentNode.prev = None
                currentNode = currentNode.next
            self.head = None
            self.tail = None
            print("Entire DLL is deleted successfully")


doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)
print([node.value for node in doublyLL])
doublyLL.insertNode(0, 0)
doublyLL.insertNode(10, 0)
doublyLL.insertNode(1, 1)
doublyLL.insertNode(2, 0)
doublyLL.insertNode(4, 1)
doublyLL.insertNode(20, 2)
print([node.value for node in doublyLL])
# doublyLL.deleteElement(0)
# doublyLL.deleteElement(1)
doublyLL.deleteElement(3)
print([node.value for node in doublyLL])
doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])
# doublyLL.forwardtraverseDLL()
# doublyLL.reversetraverseDLL()
# print(doublyLL.searchElementDLL(10))
