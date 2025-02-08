import collections
from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.numberToIndex = collections.defaultdict(SortedSet)
        self.indexToNumber = {}
        

    def change(self, index: int, number: int) -> None:
        if index in self.indexToNumber:
            previousNumber = self.indexToNumber[index]
            self.numberToIndex[previousNumber].remove(index)
            if not self.numberToIndex[previousNumber]:
                del self.numberToIndex[previousNumber]
        
        self.numberToIndex[number].add(index)
        self.indexToNumber[index] = number

    def find(self, number: int) -> int:
        if number in self.numberToIndex:
            return self.numberToIndex[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)