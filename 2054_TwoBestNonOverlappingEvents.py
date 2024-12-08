from typing import List
import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        heap = []
        ans = 0
        maxVal = 0
        for event in events:
            
            while heap and heap[0][0]<event[0]:
                maxVal = max(maxVal, heap[0][1])
                heapq.heappop(heap)

            ans = max(maxVal + event[2], ans)

            heapq.heappush(heap, event[1:])
        
        return ans