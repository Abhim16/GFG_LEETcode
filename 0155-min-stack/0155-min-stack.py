class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min = []
        
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if len(self.min) == 0 or self.min[-1]>= self.main_stack[-1]:
            self.min.append(val)
        

    def pop(self) -> None:
        if len(self.min)!=0 and self.min[-1] == self.main_stack[-1]:
            self.min.pop()
        if len(self.main_stack)!=0:
            self.main_stack.pop()
        

    def top(self) -> int:
        if len(self.main_stack)!=0:
            return self.main_stack[-1]
        

    def getMin(self) -> int:
        if len(self.min)!=0:
            return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()