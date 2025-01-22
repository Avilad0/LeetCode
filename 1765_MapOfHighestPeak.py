from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n = len(isWater), len(isWater[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        heights = [[-1]*n for _ in range(m)]

        queue = deque()        
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i,j))
                    heights[i][j]=0
        
        next_height = 1
        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()

                for i1,j1 in dirs:
                    x,y = i+i1, j+j1
                    if 0<=x<m and 0 <= y<n and heights[x][y] == -1:
                        heights[x][y] = next_height
                        queue.append((x, y))

            next_height += 1 

        return heights