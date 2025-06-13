from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0:
            return 0
        
        n = len(nums)
        nums.sort()

        def isValid(diff):
            count, i = 0, 0
            while i<n-1:
                if nums[i+1]-nums[i]<=diff:
                    count+=1
                    if count==p:
                        return True
                    i+=2
                else:
                    i+=1
            
            return False

        left, right = 0, nums[-1] - nums[0]

        while left<right:
            mid = (left+right)//2
            if isValid(mid):
                right = mid
            else:
                left = mid+1
        
        return right



# # MLE after 1575/1582 tests
# from functools import cache
# class Solution:
#     def minimizeMax(self, nums: List[int], p: int) -> int:
#         if p==0:
#             return 0
        
#         n = len(nums)
#         nums.sort()

#         @cache
#         def dfs(index, remaining):
#             if remaining == 0:
#                 return float('-inf')
            
#             if index >= n-1:
#                 return float('inf')
            
#             maxDiffWith = max(nums[index+1]- nums[index], dfs(index+2, remaining-1))

#             maxDiffWithout = dfs(index+1, remaining)

#             return min(maxDiffWith, maxDiffWithout)
        
#         return dfs(0,p)