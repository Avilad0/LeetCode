from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedSet = set(banned)
        count = 0
        for i in range(1,n+1):
            if i in bannedSet:
                continue
            if i <= maxSum:
                maxSum-=i
                count+=1
            else:
                return count
        
        return count