class MinStack:
    def __init__(self):
        self.stack = []
        self.minlist=[]
        
    def push(self, val: int) -> None:
        minimum = min(val, self.minlist[-1] if self.minlist else val)
        self.minlist.append(minimum)
        self.stack.append(val)

    def pop(self) -> None:
        self.minlist.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minlist[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()