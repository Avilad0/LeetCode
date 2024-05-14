from typing import List

class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                ans = max(ans, self.traverse(grid,i,j,m,n))

        return ans
    
    def traverse(self,grid,i,j,m,n):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]<1:
            return 0

        grid[i][j]*=(-1)
        ans = max( self.traverse(grid,i+1,j,m,n), self.traverse(grid,i-1,j,m,n), self.traverse(grid,i,j+1,m,n), self.traverse(grid,i,j-1,m,n) )
        grid[i][j]*=(-1)

        return grid[i][j] + ans
        

print(Solution().getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]])) #24
print(Solution().getMaximumGold(grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])) #28
print(Solution().getMaximumGold(grid = [[1,0,7,0,0,0],
                                        [2,0,6,0,1,0],
                                        [3,5,6,7,4,2],
                                        [4,3,1,0,2,0],
                                        [3,0,5,0,20,0]])) #60
