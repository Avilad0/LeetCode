from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
            
        m,n = len(image), len(image[0])

        pixelToChange = image[sr][sc]
        queue = deque([(sr,sc)])
        while queue:
            (r,c) = queue.popleft()
            
            if r>=0 and r<m and c>=0 and c<n and image[r][c] == pixelToChange:
                image[r][c] = color

                for i in [-1,1]: 
                    queue.append((r+i,c))
                    queue.append((r,c+i))

        return image