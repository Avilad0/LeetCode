from typing import List

# # DFS using mark/visited array (or use hashset), tc: O(mn),  sc: O(mn) 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])

        dirs= ((0,1),(1,0),(0,-1),(-1,0))
        
        def dfs(i,j, prev, mark):
            if i<0 or i>=m or j<0 or j>=n or mark[i][j] or heights[i][j]<prev:
                return
            
            mark[i][j]=True
            for (di, dj) in dirs:
                dfs(i+di, j+dj, heights[i][j], mark)


        intoTopAndLeft = [[False]*n for _ in range(m)]
        for i in range(m):
            dfs(i,0,0,intoTopAndLeft)
        for j in range(1,n):
            dfs(0,j,0,intoTopAndLeft)

        intoBottomAndRight = [[False]*n for _ in range(m)]
        for i in range(m):
            dfs(i,n-1,0, intoBottomAndRight)
        for j in range(n-1):
            dfs(m-1,j,0, intoBottomAndRight)

        ans = []
        for i in range(m):
            for j in range(n):
                if intoTopAndLeft[i][j] and intoBottomAndRight[i][j]:
                    ans.append([i,j])
                
        return ans