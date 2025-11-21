from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        m, n = len(heights), len(heights[0])
        heap = [(0,0,0)]    #(diff, row, col)

        visited = [[False]*n for _ in range(m)]

        while len(heap)>0:
            (currMaxDiff, row, col) = heapq.heappop(heap)
            if visited[row][col]:
                continue
            visited[row][col] = True

            if row==m-1 and col==n-1:
                return currMaxDiff

            for (dx, dy) in dirs:
                newRow, newCol = row+dx, col+dy
                if newRow>=0 and newRow<m and newCol>=0 and newCol<n and not visited[newRow][newCol]:
                    heapq.heappush(heap, ( max(currMaxDiff, abs(heights[row][col]-heights[newRow][newCol])) ,newRow, newCol))

        return -1

print(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))