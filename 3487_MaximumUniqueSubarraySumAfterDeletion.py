from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniques = set()

        score = 0
        maxNeg = -float('inf')
        for num in nums:
            if num>=0 and num not in uniques:
                score+=num
                uniques.add(num)
            else:
                maxNeg = max(maxNeg, num)
        
        return score if len(uniques)!=0 else maxNeg