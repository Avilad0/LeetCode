from typing import List
from collections import Counter

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        toInclude = dict(Counter(sorted(nums, reverse=True)[:k]))
        ans = []
        for num in nums:
            if num in toInclude:
                ans.append(num)
                toInclude[num]-=1
                if toInclude[num]==0:
                    toInclude.pop(num)
        return ans