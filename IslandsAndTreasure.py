from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        
        m,n = len(grid), len(grid[0])

        def traverse(i,j, dist):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]<=dist:
                return
            
            grid[i][j]=dist
            
            for (di,dj) in dirs:
                traverse(i+di, j+dj, dist+1)


        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    for (di, dj) in dirs:
                        traverse(di+i,dj+j,1)