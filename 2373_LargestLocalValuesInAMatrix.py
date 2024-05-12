from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []

        for i in range(1,n-1):
            maxLocal_temp = []
            for j in range(1,n-1):
                maxLocal_temp.append(max( grid[i-1][j-1:j+2] + grid[i][j-1:j+2] +grid[i+1][j-1:j+2] ))
                # maxLocal_temp.append(max(grid[i-1][j-1],
                #                      grid[i-1][j],
                #                      grid[i-1][j+1],
                #                      grid[i][j-1],
                #                      grid[i][j],
                #                      grid[i][j+1],
                #                      grid[i+1][j-1],
                #                      grid[i+1][j],
                #                      grid[i+1][j+1]))
                
            maxLocal.append(maxLocal_temp)

        return maxLocal

print(Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
print(Solution().largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))