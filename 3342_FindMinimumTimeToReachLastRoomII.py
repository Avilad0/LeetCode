from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        pq = [(0,1,0,0)]  #currCost, movingCost,i,j
        minTime = [[float('inf')]*m for _ in range(n)] 

        while pq:
            (currCost,movingCost, i,j) = heapq.heappop(pq)

            if i==n-1 and j==m-1:
                return currCost

            for d in dirs:
                ni, nj = i+d[0], j+d[1]
                if 0<=ni<n and 0<=nj<m:
                    nextCost = max(currCost,moveTime[ni][nj]) + movingCost
                    if minTime[ni][nj]>nextCost:
                        heapq.heappush(pq, (nextCost, movingCost^3, ni, nj))
                        minTime[ni][nj] = nextCost

        return float('inf')