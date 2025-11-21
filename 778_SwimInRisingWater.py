from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n<1:
            return -1
            
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        minHeap = [(grid[0][0],0,0)] #(minTime, row, col)
        visited = [[False]*n for _ in range(n)]

        while minHeap:
            (minLevel, row, col) = heapq.heappop(minHeap)
            if visited[row][col]:
                continue
            visited[row][col] = True

            if row==n-1 and col==n-1:
                return minLevel

            for (di, dj) in dirs:
                nRow, nCol = row+di, col+dj
                if nRow>=0 and nRow<n and nCol>=0 and nCol<n and (not visited[nRow][nCol]):
                    heapq.heappush(minHeap, (max(grid[nRow][nCol], minLevel),nRow, nCol))

        return -1        