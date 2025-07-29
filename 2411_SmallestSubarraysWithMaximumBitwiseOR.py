from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        minBitPos = [-1]*31
        ans = [0]*n
        for i in range(n-1,-1,-1):
            maxRequiredBitPos = i
            for bit in range(31):
                if (1<<bit) & nums[i]:
                    minBitPos[bit] = i
                else:
                    maxRequiredBitPos = max(maxRequiredBitPos, minBitPos[bit])
            
            ans[i] = maxRequiredBitPos - i + 1

        return ans