class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minlist = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minlist.append(val if not self.minlist else min(val, self.minlist[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minlist.pop()
        
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