from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m,n= len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        max_fish = 0

        def dfs(i: int, j: int) -> int:
            if i<0 or i>=m or j<0 or j>=n or visited[i][j] or grid[i][j]==0:
                return 0
            
            visited[i][j]=True
            
            return grid[i][j] + dfs(i+1, j) + dfs(i-1, j) + dfs(i,j-1) + dfs(i,j+1)

        for i in range(m):
            for j in range(n):                
                fish = dfs(i,j)
                if fish>max_fish:
                    max_fish=fish

        return max_fish