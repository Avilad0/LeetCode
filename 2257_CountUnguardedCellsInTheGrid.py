from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # N = not Gaurded, G = Guard, GD = Guarged, W=Wall

        grid = [['N']*n for _ in range(m)]

        for w in walls:
            grid[w[0]][w[1]] = 'W'
        
        for g in guards:
            grid[g[0]][g[1]] = 'G'

        for g in guards:
            i,j=g[0],g[1]

            ii,jj=i+1,j
            while ii<m and grid[ii][jj]!='W' and grid[ii][jj]!='G':
                grid[ii][jj]='GD'
                ii+=1
            
            ii,jj=i-1,j
            while ii>=0 and grid[ii][jj]!='W' and grid[ii][jj]!='G':
                grid[ii][jj]='GD'
                ii-=1
                
            ii,jj=i,j+1
            while jj<n and grid[ii][jj]!='W' and grid[ii][jj]!='G':
                grid[ii][jj]='GD'
                jj+=1
                
            ii,jj=i,j-1
            while jj>=0 and grid[ii][jj]!='W' and grid[ii][jj]!='G':
                grid[ii][jj]='GD'
                jj-=1
            
        ans =0 
        for row in grid:
            ans+= row.count('N')
        
        return ans