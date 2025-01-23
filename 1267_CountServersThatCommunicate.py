from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        row_freq, col_freq = [0]*m, [0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_freq[i]+=1
                    col_freq[j]+=1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row_freq[i]>1 or col_freq[j]>1):
                    ans+=1
                    
        return ans