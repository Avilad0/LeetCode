from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestSquareStreat = -1
        for num in nums:
            length = 1
            while num*num in numsSet:
                length+=1
                num*=num
            
            if length>longestSquareStreat:
                longestSquareStreat=length

        return longestSquareStreat if longestSquareStreat>1 else -1