class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        m,n = len(grid), len(grid[0])

        maxArea = 0

        def getArea(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
                return 0

            grid[i][j]=0
            area=1
            for (di, dj) in dirs:
                area+=getArea(i+di,j+dj)

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    maxArea = max(maxArea, getArea(i,j))

        return maxArea
        