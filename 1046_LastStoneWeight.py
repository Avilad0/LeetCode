from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            x,y= -heapq.heappop(heap), -heapq.heappop(heap)
            newS = abs(x-y)
            if newS>0:
                heapq.heappush(heap, -newS)
        
        return 0 if len(heap)==0 else -heap[0]