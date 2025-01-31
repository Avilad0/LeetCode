from typing import List

class Solution:

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    def dfs(self, grid: List[List[int]], i: int, j: int, islandNumber: int) -> int:
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]!=1:
            return 0
        
        grid[i][j] = islandNumber
        size = 1
        for (u,v) in self.dirs:
            size += self.dfs(grid, i+u, j+v, islandNumber)

        return size

    def largestIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        islandNumber = 2
        islandSizes = {}

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    islandSizes[islandNumber] = self.dfs(grid, i, j, islandNumber)
                    islandNumber+=1
        
        if islandNumber==2:
            return 1
        
        if islandNumber==3:
            return islandSizes[2] if (islandSizes[2]==(m*n)) else (islandSizes[2]+1)


        maxSize = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    neighbourIslands = set()
                    for (u,v) in self.dirs:
                        if (i+u)>=0 and (i+u)<m and (j+v)>=0 and (j+v)<n and grid[i+u][j+v]!=0:
                            neighbourIslands.add(grid[i+u][j+v])
                    
                    newIslandSize = 1
                    for x in neighbourIslands:
                        newIslandSize+=islandSizes[x]
                    
                    if newIslandSize > maxSize:
                        maxSize = newIslandSize
        
        return maxSize