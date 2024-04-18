from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        ans= 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    ans+=4
                    if i>0 and grid[i-1][j]==1:
                        ans-=2
                    if j>0 and grid[i][j-1]==1:
                        ans-=2

        return ans
    

    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     r = len(grid)
    #     c = len(grid[0])

    #     ans= 0
    #     for i in range(r):
    #         for j in range(c):
    #             if grid[i][j]==1:
    #                 if i==0 or grid[i-1][j]==0:
    #                     ans+=1
    #                 if i==r-1 or grid[i+1][j]==0:
    #                     ans+=1
    #                 if j==0 or grid[i][j-1]==0:
    #                     ans+=1
    #                 if j==c-1 or grid[i][j+1]==0:
    #                     ans+=1

    #     return ans
    
print(Solution().islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(Solution().islandPerimeter(grid = [[1]]))
