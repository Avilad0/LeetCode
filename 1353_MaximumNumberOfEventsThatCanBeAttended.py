from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        minStartDay, maxEndDay =events[0][0], max(events, key = lambda x:x[1])[1]
        n, eventIndex = len(events), 0
        minHeap = []
        
        ans = 0
        for currDay in range(minStartDay, maxEndDay+1):
            while minHeap and minHeap[0] < currDay:
                heapq.heappop(minHeap)
            
            while eventIndex<n and events[eventIndex][0]==currDay:
                heapq.heappush(minHeap, events[eventIndex][1])
                eventIndex+=1
            
            if minHeap:
                heapq.heappop(minHeap)
                ans+=1

        return ans
    

print(Solution().maxEvents(events= [[1,2],[2,3],[3,4],[1,2]])) #Output: 4
