import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] #for smaller nums than median with median at top
        self.minHeap = [] #for greater nums than median, with median at top

    def addNum(self, num: int) -> None:
        if len(self.minHeap)==0 or num>=self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        

        if len(self.minHeap)-len(self.maxHeap)==2:
            tempNum = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -tempNum)
        elif len(self.maxHeap)-len(self.minHeap)==2:
            tempNum = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -tempNum)


    def findMedian(self) -> float:
        if len(self.minHeap)==len(self.maxHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2
        elif len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()