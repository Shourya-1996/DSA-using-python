class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stacknumber):
        if len(self.stacks[stacknumber]) > 0:
            return self.stacks[stacknumber].pop()
        else:
            return None


custstack = PlateStack(2)
custstack.push(1)
custstack.push(2)
custstack.push(3)
custstack.push(4)
print(custstack.pop_at(0))
print(custstack)
