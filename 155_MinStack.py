class MinStack:

    def __init__(self):
        self.stck = []
        self.minStck = []

    def push(self, val: int) -> None:
        self.stck.append(val)
        if not self.minStck or val<=self.minStck[-1]:
            self.minStck.append(val)        

    def pop(self) -> None:
        if self.stck[-1]==self.minStck[-1]:
            self.minStck.pop()
        self.stck.pop()

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return self.minStck[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()