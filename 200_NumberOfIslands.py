from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans =0 
        r = len(grid)
        c = len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]=='0':
                return
            grid[i][j]='0'
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)


        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    dfs(i,j)
                    ans+=1

        return ans 

print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],  ["0","0","1","0","0"],["0","0","0","1","1"]]))
print(Solution().numIslands([["1"]]))
