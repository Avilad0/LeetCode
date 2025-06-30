from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        ans = 0
        for key, f in freq.items():
            if key+1 in freq:
                ans = max(ans, f + freq[key+1])
        
        return ans