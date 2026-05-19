class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        m,n = len(matrix), len(matrix[0])

        memo = {}
        def dfs(i,j):
            if (i,j) not in memo:
                maxPath = 1
                for (di,dj) in dirs:
                    ni, nj = i+di, j+dj
                    if ni>=0 and ni<m and nj>=0 and nj<n and matrix[i][j]<matrix[ni][nj]:
                        maxPath = max(maxPath, 1+dfs(ni,nj))
                
                memo[(i,j)] = maxPath

            return memo[(i,j)]
        
        maxPath = 0
        for i in range(m):
            for j in range(n):
                maxPath = max(maxPath, dfs(i,j))
        
        return maxPath