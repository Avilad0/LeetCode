from typing import List

#BFS
from collections import  deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        
        m,n = len(grid), len(grid[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        
        dist = 1
        while q:
            for _ in range(len(q)):
                (i,j) = q.popleft()
                for (di,dj) in dirs:
                    ni, nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj]>dist:
                        grid[ni][nj]=dist
                        q.append((ni,nj))
                
            dist+=1


# #BFS
# from collections import  deque
# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         dirs = ((0,1),(0,-1),(1,0),(-1,0))
        
#         m,n = len(grid), len(grid[0])

#         q = deque()

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==0:
#                     for (di,dj) in dirs:
#                         ni, nj = i+di, j+dj
#                         if 0<=ni<m and 0<=nj<n:
#                             q.append((ni,nj,1))
        
#         while q:
#             (i,j,dist) = q.popleft()
#             if grid[i][j]<=dist:
#                 continue
#             grid[i][j]=dist
#             for (di,dj) in dirs:
#                 ni, nj = i+di, j+dj
#                 if 0<=ni<m and 0<=nj<n:
#                     q.append((ni,nj,dist+1))

#DFS
# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         dirs = ((0,1),(0,-1),(1,0),(-1,0))
        
#         m,n = len(grid), len(grid[0])

#         def traverse(i,j, dist):
#             if i<0 or i>=m or j<0 or j>=n or grid[i][j]<=dist:
#                 return
            
#             grid[i][j]=dist
            
#             for (di,dj) in dirs:
#                 traverse(i+di, j+dj, dist+1)


#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==0:
#                     for (di, dj) in dirs:
#                         traverse(di+i,dj+j,1)