from typing import List

# TC = O(N), SC = O(1)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        setBits = 0
        for num in nums:
            setBits |= num
        
        return setBits<<(len(nums)-1)
    

# TC = O(N * 2**N), SC = O(n)
# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         n = len(nums)

#         def traverse(i: int, currentXor:int ):
#             if i==n:
#                 return currentXor
            
#             return traverse(i+1, currentXor) + traverse(i+1, currentXor^nums[i])

#         return traverse(0,0)