class Heap:
    def __init__(self, size):
        self.customList = size * [None]
        self.heapsize = 0
        self.maxSize = size + 1


def peekOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]


def sizeOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapsize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapsize+1):
            print(rootNode.customList[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            # swapping parent node and current Node
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapsize + 1 == rootNode.maxSize:
        return "Binary Heap is full"
    rootNode.customList[rootNode.heapsize + 1] = nodeValue
    rootNode.heapsize += 1
    heapifyTreeInsert(rootNode, rootNode.heapsize, heapType)
    return "value is inserted"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    if rootNode.heapsize < leftIndex:
        return
    # if root node has only 1 child
    elif rootNode.heapsize == leftIndex:
        if heapType == "min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]
            return
    else:
        # root node has 2 children
        if heapType == "min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
    heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapsize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapsize]
        rootNode.customList[rootNode.heapsize] = None
        rootNode.heapsize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode


def deleteEntireHeap(rootNode):
    rootNode.customList = None


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 4, "max")
insertNode(newBinaryHeap, 5, "max")
insertNode(newBinaryHeap, 2, "max")
insertNode(newBinaryHeap, 1, "max")
levelOrderTraversal(newBinaryHeap)
print("------------")
print(extractNode(newBinaryHeap, "max"))
# deleteEntireHeap(newBinaryHeap)
heapifyTreeExtract(newBinaryHeap, 1, "max")
levelOrderTraversal(newBinaryHeap)
# print(sizeOfHeap(newBinaryHeap))
