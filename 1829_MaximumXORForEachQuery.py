from typing import List

# same complexity but 1st works with just 1 loop

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maximumNumber = (1<<maximumBit) - 1
        xor = 0
        n=len(nums)
        ans = [0]*n
        
        for i in range(n):
            xor ^= nums[i]
            ans[n-1-i] = maximumNumber ^ xor

        return ans

# class Solution:
#     def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
#         xor = 0
#         for num in nums:
#             xor^=num
        
#         maximumNumber = (1<<maximumBit) - 1
#         ans = []
#         for i in range(len(nums)-1,-1,-1):
#             ans.append(maximumNumber ^ xor)
#             xor ^= nums[i]

#         return ans