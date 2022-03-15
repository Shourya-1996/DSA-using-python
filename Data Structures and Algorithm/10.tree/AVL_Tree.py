import queue_using_linkedList as queue


class AVLnode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1


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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.left
    disbalanceNode.left = disbalanceNode.left.right
    newRoot.right = disbalanceNode
    disbalanceNode.height = 1 + \
        max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.right
    disbalanceNode.right = disbalanceNode.right.left
    newRoot.left = disbalanceNode
    disbalanceNode.height = 1 + \
        max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)


def insertNode(rootNode, value):
    if not rootNode:
        return AVLnode(value)
    elif value < rootNode.data:
        rootNode.left = insertNode(rootNode.left, value)
    else:
        rootNode.right = insertNode(rootNode.right, value)

    rootNode.height = 1 + max(getHeight(rootNode.left),
                              getHeight(rootNode.right))
    balance = getBalance(rootNode)
    if balance > 1 and value < rootNode.left.data:
        return rightRotate(rootNode)
    if balance > 1 and value > rootNode.left.data:
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance < -1 and value > rootNode.right.data:
        return leftRotate(rootNode)
    if balance < -1 and value < rootNode.right.data:
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode


def getMinValue(rootNode):
    if rootNode is None or rootNode.left is None:
        return rootNode
    return getMinValue(rootNode.left)


def deleteNode(rootNode, value):
    if not rootNode:
        return rootNode
    elif value < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, value)
    elif value > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, value)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        elif rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = getMinValue(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    rootNode.height = 1 + max(getHeight(rootNode.left),
                              getHeight(rootNode.right))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.left) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.right) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.left) < 0:
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.right) > 0:
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode


def deleteEntireAVL(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "AVL Tree is deleted"


newAVL = AVLnode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = insertNode(newAVL, 30)
newAVL = deleteNode(newAVL, 15)
levelOrderTraversal(newAVL)
deleteEntireAVL(newAVL)
levelOrderTraversal(newAVL)
