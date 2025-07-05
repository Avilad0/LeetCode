from typing import List
from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:

        freq = defaultdict(int)
        for num in arr:
            freq[num]+=1
        
        ans = -1
        for num, f in freq.items():
            if f==num and num>ans:
                ans = num
        
        return ans