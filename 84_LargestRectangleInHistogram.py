from typing import List

# tc=O(n), sc=O(n), monotonic stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack=[]
        leftMins = [-1]*n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                leftMins[i] = stack[-1]
            stack.append(i)

        stack=[]
        rightMins = [n]*n
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                rightMins[i]=stack[-1]
            stack.append(i)
        
        maxRect = 0
        for i in range(n):
            maxRect = max(maxRect, heights[i]* (rightMins[i]-leftMins[i]-1))
        
        return maxRect
    
# tc=O(n), sc=O(n), monotonic stack - more optimal
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxRect = 0

        stack=[] #(heightIndexOfCurrentRectangleHeight)
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]]>heights[i]):
                h = heights[stack.pop()]
                w = i if not stack else (i-1 - stack[-1]) #(stack[-1] + 1 or 0) to i-1
                maxRect = max(maxRect, h*w)

            stack.append(i)

        return maxRect