from typing import List


#O(n)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        maxNum, currLen = nums[0], 1

        for i in range(1,n):
            if nums[i]>maxNum:
                ans = currLen = 1
                maxNum = nums[i]
            elif nums[i]==maxNum:
                if nums[i]==nums[i-1]:
                    currLen+=1
                    ans = max(ans, currLen)
                else:
                    currLen=1

        return ans
    

# #O(n)
# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = 1

#         currNum, maxNum, left = nums[0], nums[0], 0
#         for right in range(1,n):
#             if nums[right] != nums[left]:
#                 currNum = nums[right]
#                 left = right

#             if currNum==maxNum:
#                 ans = max(ans, right-left+1)
#             elif currNum>maxNum:
#                 maxNum = currNum
#                 ans = right-left+1

#         return ans
