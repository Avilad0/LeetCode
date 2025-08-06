class SegmentTrees:
    def __init__(self,arr):
        self.n=len(arr)
        self.segTree = [0]*(4*self.n)
        self.build(0, 0, self.n-1, arr)
    
    def build(self, index, left, right, arr):
        if left==right:
            self.segTree[index] = arr[left]
            return 
        
        mid = (left+right)//2
        self.build(2*index +1, left, mid, arr)
        self.build(2*index +2, mid+1, right, arr)

        self.segTree[index] = max(self.segTree[2*index+1], self.segTree[2*index + 2])
        return 

    def query(self, index, left, right, queryLeft, queryRight):
        if left>=queryLeft and right<=queryRight:
            return self.segTree[index]

        if left>queryRight or right<queryLeft:
            return -float('inf')

        mid = (left+right)//2
        return max(self.query(2*index+1, left,mid, queryLeft, queryRight), self.query(2*index+2, mid+1, right, queryLeft, queryRight))