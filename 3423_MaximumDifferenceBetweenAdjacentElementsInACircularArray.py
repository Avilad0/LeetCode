from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxDiff = abs(nums[0]-nums[-1])
        for i in range(n-1):
            maxDiff = max(maxDiff, abs(nums[i]-nums[i+1]))
        return maxDiff