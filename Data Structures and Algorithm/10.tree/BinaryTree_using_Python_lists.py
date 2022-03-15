class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxsize = size

    def __str__(self):
        values = [str(x) for x in self.customList[1:]]
        return ",".join(values)

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return "Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "value is inserted"

    def search(self, nodeValue):
        for i in self.customList:
            if i == nodeValue:
                return "Success"
        return "Not Found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in self.customList[index:self.lastUsedIndex+1]:
            print(i)

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "Binary Tree is Empty"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "node is deleted"

    def delteBT(self):
        self.customList = None
        return "Binary Tree is deleted"


newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
# print(newBT)
# print(newBT.search("Cold"))
newBT.deleteNode("Drinks")
newBT.levelOrderTraversal(1)
print(newBT.delteBT())
