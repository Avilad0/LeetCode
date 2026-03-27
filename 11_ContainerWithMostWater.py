from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left,right = 0,n-1
        maxStorage = 0
        while left<right:
            maxStorage = max( min(heights[left], heights[right]) * (right-left) , maxStorage )
            
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1

        return maxStorage