from typing import List
from math import ceil

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        if n==1:
            return quantities[0]

        def isPossibleDistribution(x):
            count = 0
            for q in quantities:
                count+= ceil(q/x)
            
            return count<=n


        left,right = 1, max(quantities)
        minn = right
        while left<=right:
            mid = (left+right)//2
            if isPossibleDistribution(mid):
                minn= mid
                right = mid-1
            else:
                left = mid+1
            
        return minn

print(Solution().minimizedMaximum(n = 7, quantities = [15,10,10]))