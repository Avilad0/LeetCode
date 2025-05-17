from typing import List

#1-pass
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nextZero, nextTwo, i = 0, n-1, 0

        while i<=nextTwo:
            if nums[i]==0:
                nums[i],nums[nextZero] = nums[nextZero], nums[i]
                nextZero+=1
            elif nums[i]==2:
                nums[i],nums[nextTwo] = nums[nextTwo], nums[i]
                nextTwo-=1
                i-=1
            
            i+=1

# 2-pass
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         left, right = 0, n-1
#         while left<right:
#             while left<=right and nums[left]!=2:
#                 left+=1
            
#             while right>=left and nums[right]==2:
#                 right-=1
            
#             if left<right:
#                 nums[left], nums[right] = nums[right], nums[left]
        

#         left = 0
#         while left<right:
#             while left<=right and nums[left]==0:
#                 left+=1
#             while right>=left and nums[right]==1:
#                 right-=1
            
#             if left<right:
#                 nums[left], nums[right] = nums[right], nums[left]
