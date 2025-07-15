from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        nextAvaialbleChair = 0
        middleChairsAvailable = []
        occupiedChairs = []

        indexedTimes = [[times[i][0],times[i][1],i] for i in range(n)]
        indexedTimes.sort(key = lambda x:x[0])

        for [start, end, index] in indexedTimes:

            while occupiedChairs and occupiedChairs[0][0]<=start:
                ( _, chairFreed) = heapq.heappop(occupiedChairs)
                heapq.heappush(middleChairsAvailable, chairFreed)

            if middleChairsAvailable:
                chair = heapq.heappop(middleChairsAvailable)
            else:
                chair = nextAvaialbleChair
                nextAvaialbleChair+=1
            
            if index == targetFriend:
                return chair
            else:
                heapq.heappush(occupiedChairs, (end, chair) )