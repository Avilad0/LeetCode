from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0]*k for _ in range(k)]
        maxLen = 0

        for num in nums:
            curr = num%k
            for prev in range(k):
                dp[curr][prev] = dp[prev][curr]+1
                maxLen = max(maxLen, dp[curr][prev])
            
        return maxLen