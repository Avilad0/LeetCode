from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1 or nums[0]<=nums[-1]:
            return nums[0]

        left, right = 0, n-1
        while left<right:
            mid = (left+right)//2
            # always check with right and not left
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid+1
        
        print(left, right)
        return nums[left]



# # same as above but more elaborate.
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         if n==1 or nums[0]<nums[-1]:
#             return nums[0]
        
#         ans = nums[0]
#         left, right = 0, len(nums)-1

#         while left<=right:
#             if nums[left]<nums[right]:
#                 ans=min(ans, nums[left])
#                 break

#             mid = (left+right)//2
#             ans = min(ans, nums[mid])

#             if nums[mid]<nums[right]:
#                 right=mid-1
#             else:
#                 left=mid+1
        
#         return ans