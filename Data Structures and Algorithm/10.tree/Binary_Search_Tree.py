import queue_using_linkedList as queue


class BSTnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertNode(rootNode, value):
    if rootNode.data is None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BSTnode(value)
        else:
            insertNode(rootNode.left, value)
    else:
        if rootNode.right is None:
            rootNode.right = BSTnode(value)
        else:
            insertNode(rootNode.right, value)
    return "Node is inserted"


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        custom = queue.Queue()
        custom.enqueue(rootNode)
        while not custom.isEmpty():
            root = custom.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                custom.enqueue(root.value.left)
            if root.value.right is not None:
                custom.enqueue(root.value.right)


def searchNode(rootNode, value):
    if rootNode.data == value:
        print("found")
    elif value < rootNode.data:
        if rootNode.left.data == value:
            print("found")
        else:
            searchNode(rootNode.left, value)
    else:
        if rootNode.right.data == value:
            print("found")
        else:
            searchNode(rootNode.right, value)


def minvalueNode(rootNode):
    current = rootNode
    while current.left is not None:
        current = current.left
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = minvalueNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    return rootNode


def deleteBST(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "BST deleted"


newBST = BSTnode(None)
insertNode(newBST, 70)
insertNode(newBST, 60)
insertNode(newBST, 90)
insertNode(newBST, 40)
insertNode(newBST, 50)
insertNode(newBST, 100)
deleteBST(newBST)
# print(newBST.data)
# print(newBST.left.data)
# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
levelOrderTraversal(newBST)
