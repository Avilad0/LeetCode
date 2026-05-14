from typing import List

# tc=O(n), sc=O(1), same as below
class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        ans = 0

        #leftToright
        maxHeight, maxHeightIndex, currStore = 0, -1, 0

        for i in range(n):
            if height[i]>=maxHeight:
                ans+=currStore
                currStore=0
                maxHeight, maxHeightIndex = height[i], i
            else:
                currStore+=maxHeight-height[i]

        #rightToLeft
        currMaxHeight = 0
        for i in range(n-1, maxHeightIndex,-1):
            if height[i]>=currMaxHeight:
                currMaxHeight = height[i]
            else:
                ans+=currMaxHeight-height[i]
        
        return ans

# tc=O(n), sc=O(1), same as above
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l = len(height)
#         if l<=2:
#             return 0
        
#         ans = 0
#         temp_ans = 0
#         h_in = 0
#         for i in range(1,l):
#             if height[i]>=height[h_in]:
#                 ans += temp_ans
#                 temp_ans=0
#                 h_in = i
#             else:
#                 temp_ans+=height[h_in] - height[i]

#         if temp_ans>0:
#             m = height[l-1]
#             for i in range(l-2,h_in,-1):
#                 if height[i]>m:
#                     m = height[i]
#                 else:
#                     ans+= m - height[i]
#         return ans


# tc=O(n), sc=O(1)
# class Solution:
#     def trap(self, height: List[int]) -> int:
        
#         ans = 0
#         left, right = 0, len(height)-1
#         leftMax, rightMax = height[left], height[right]

#         while left<right:

#             if leftMax<rightMax:
#                 left+=1
#                 leftMax=max(leftMax, height[left])
#                 ans+=leftMax-height[left]
#             else:
#                 right-=1
#                 rightMax=max(rightMax, height[right])
#                 ans+=rightMax-height[right]

#         return ans
    

print(Solution().trap([2,0,2]))
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,0,3,2,5]))