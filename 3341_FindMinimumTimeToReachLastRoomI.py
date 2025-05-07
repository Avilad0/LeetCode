from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        pq = [(0,0,0)]  #cost,i,j
        minTime = [[float('inf')]*m for _ in range(n)] 

        while pq:
            (currCost,i,j) = heapq.heappop(pq)

            if i==n-1 and j==m-1:
                return currCost

            for d in dirs:
                ni, nj = i+d[0], j+d[1]
                if 0<=ni<n and 0<=nj<m:
                    nextCost = max(currCost,moveTime[ni][nj])+1
                    if minTime[ni][nj]>nextCost:
                        heapq.heappush(pq, (nextCost, ni, nj))
                        minTime[ni][nj] = nextCost

        return float('inf')
    

print(Solution().minTimeToReach([[0,0,0],[0,0,0]]))  # 3