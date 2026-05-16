from typing import List

import heapq
# import math

#tc=O(nlogk), sc=O(k) - maxHeap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i in range(len(points)):
            # dist = math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1])
            dist = points[i][0]*points[i][0] + points[i][1]*points[i][1] #skip sqrt is also fine as only want for comparison

            heapq.heappush(maxHeap, (-dist,i))
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        
        return [points[h[1]] for h in maxHeap] 