class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))
        

        

    def pop(self) -> None:
        self.stack_length = len(self.stack) - 1            

        self.stack = self.stack[0:self.stack_length]
        self.minStack = self.minStack[0:self.stack_length]

    def top(self) -> int:
        self.stack_length = len(self.stack) -1
        return self.stack[self.stack_length]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
