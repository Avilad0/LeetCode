from typing import List

from collections import deque
# 0-1 BFS : tc=O(m*n), sc=O(m*n)
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        dirs = {1:(0,1), 2:(0,-1), 3:(1,0), 4:(-1,0)}

        m,n = len(grid), len(grid[0])

        minCost = [[float('inf') for _ in range(n)] for __ in range(m)]
        minCost[0][0]=0

        dq = deque([(0,0)])
        while dq:
            (r, c) = dq.popleft()

            for i in range(1,5):
                nr, nc = r+dirs[i][0], c+dirs[i][1]
                nCost = (0 if i==grid[r][c] else 1)
                if nr>=0 and nr<m and nc>=0 and nc<n and minCost[nr][nc]>minCost[r][c]+nCost:
                    minCost[nr][nc]=minCost[r][c]+nCost
                    if nCost==1:
                        dq.append((nr,nc))
                    else:
                        dq.appendleft((nr,nc))
        
        return minCost[m-1][n-1]



# # import heapq

# # Dijkstra's : tc=O(m*n*log(m*n)), sc=O(m*n)
# class Solution:
#     def minCost(self, grid: List[List[int]]) -> int:
#         dirs = {1:(0,1), 2:(0,-1), 3:(1,0), 4:(-1,0)}

#         m,n = len(grid), len(grid[0])

#         minCost = [[float('inf') for _ in range(n)] for __ in range(m)]

#         pq = [(0, 0,0)]     #minHeap: cost, row, col
#         while pq:
#             (cost, r, c) = heapq.heappop(pq)
#             if r==m-1 and c==n-1:
#                 return cost
            
#             if minCost[r][c]<=cost:
#                 continue

#             minCost[r][c]=cost
#             for i in range(1,5):
#                 nr, nc = r+dirs[i][0], c+dirs[i][1]
#                 nCost = cost+ (0 if i==grid[r][c] else 1)
#                 if nr>=0 and nr<m and nc>=0 and nc<n and minCost[nr][nc]>nCost:
#                     heapq.heappush(pq, (nCost, nr, nc))
        
#         return -1