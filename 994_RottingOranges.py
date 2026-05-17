from typing import List

from collections import deque

# tc=O(m*n), sc=O(m*n), BFS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = ((0,1),(0,-1),(1,0),(-1,0))

        m,n=len(grid), len(grid[0])

        time = 0 

        q = deque()
        freshOrange = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    freshOrange+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        
        while freshOrange>0 and q:
            for _ in range(len(q)):
                (i,j) = q.popleft()

                for (di, dj) in dirs:
                    ni, nj = i+di, j+dj
                    if ni>=0 and ni<m and nj>=0 and nj<n and grid[ni][nj]==1:
                        grid[ni][nj]=2
                        freshOrange-=1
                        q.append((ni,nj))
        
            time+=1


        return time if freshOrange==0 else -1

# # tc=O(m*n), sc=O(m*n), DFS
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         dirs = ((0,1),(0,-1),(1,0),(-1,0))

#         m,n=len(grid), len(grid[0])

#         def traverse(i,j, dist):
#             if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or (2<=grid[i][j]<=dist+2):
#                 return

#             #mark dist as +2 because 2 is already taken for rotten, so we start 3 as dist=1, 4 as dist=2 ..
#             grid[i][j]=dist+2

#             for (di, dj) in dirs:
#                 traverse(i+di, j+dj, dist+1)
            

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==2:
#                     for (di,dj) in dirs:
#                         traverse(i+di, j+dj, 1)

#         maxDist = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==1:
#                     return -1
#                 elif grid[i][j]!=0:
#                     maxDist=max(maxDist, grid[i][j]-2)

#         return maxDist