from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        ans = m*(1<<(n-1))

        for j in range(1,n):
            c = 0 
            for i in range(m):
                if grid[i][j]==grid[i][0]:
                    c+=1
            
            if c+c<m:
                c=m-c
            
            ans+= (c*(1<<(n-j-1)))

        return ans

        #
        # m = len(grid)
        # n = len(grid[0])

        # for i in range(m):
        #     if grid[i][0] == 0:
        #         for j in range(n):
        #             grid[i][j] ^= 1
        
        # for j in range(1,n):
        #     count = 0
        #     for i in range(m):
        #             count+=grid[i][j]
            
        #     if count+count<m:
        #         for i in range(m):
        #             grid[i][j]^=1
        
        # ans = 0
        # for i in grid:
        #     t=0
        #     for j in i:
        #         t= t*2 + j
        #     ans+=t

        # return ans

print(Solution().matrixScore(grid = [[1]])) #1
print(Solution().matrixScore(grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]])) #39