class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val) 
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

stack = MinStack()


stack.push(8)
stack.push(5)
stack.push(6)
stack.push(3)

print(stack.getMin())