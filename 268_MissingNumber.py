from typing import List

# tc = O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        missing = 0
        for i in range(n):
            missing=missing^nums[i]^(i+1)
        
        return missing
    

# # tc = O(n)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         return ((n*(n+1))//2) - sum(nums)