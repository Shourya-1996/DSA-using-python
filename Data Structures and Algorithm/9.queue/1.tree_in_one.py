class MultiStack:
    def __init__(self, stacksize):
        self.numberOfstacks = 3
        self.cusList = [0]*(stacksize*self.numberOfstacks)
        self.numOfElements = [0]*self.numberOfstacks
        self.stacksize = stacksize

    def isFull(self, stacknum):
        if self.numOfElements[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.numOfElements[stacknum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stacknum):
        offset = stacknum*self.stacksize
        return offset + self.numOfElements[stacknum] - 1

    def push(self, stacknum, value):
        if self.isFull(stacknum):
            return "stack is full"
        else:
            self.numOfElements[stacknum] += 1
            self.cusList[self.indexOfTop(stacknum)] = value

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "stack is empty"
        else:
            value = self.cusList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.numOfElements[stacknum] -= 1
            return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "stack is empty"
        else:
            return self.cusList[self.indexOfTop(stacknum)]


customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(0, 0)
print(customStack.peek(1))
