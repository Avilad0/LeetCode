from typing import List

class SegmentTrees:
    def __init__(self,baskets):
        self.n=len(baskets)
        self.segTree = [0]*(4*self.n)
        self.build(0, 0, self.n-1, baskets)
    

    def build(self, index, left, right, baskets):
        if left==right:
            self.segTree[index] = baskets[left]
            return 
        
        mid = (left+right)//2
        self.build(2*index +1, left, mid, baskets)
        self.build(2*index +2, mid+1, right, baskets)

        self.segTree[index] = max(self.segTree[2*index+1], self.segTree[2*index + 2])
        return 


    def getFirstAndUpdate(self, index, left, right, val):
        if self.segTree[index]<val:
            return -1
        
        if left==right:
            self.segTree[index] = -1
            return left
        
        mid = (left+right)//2
        
        FirstIndexMatchToVal = self.getFirstAndUpdate(2*index + 1, left, mid, val)
        if FirstIndexMatchToVal==-1:
            FirstIndexMatchToVal = self.getFirstAndUpdate(2*index+2, mid+1, right, val)
        
        self.segTree[index] = max(self.segTree[2*index+1], self.segTree[2*index + 2])

        return FirstIndexMatchToVal


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        basketsSegTree = SegmentTrees(baskets)
        
        unplaced = 0
        for fruit in fruits:
            if basketsSegTree.getFirstAndUpdate(0, 0, n-1,fruit)==-1:
                unplaced+=1

        return unplaced