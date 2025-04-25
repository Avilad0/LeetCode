from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        
        n= len(nums)
        prefixSumSatisfyingNums = 0
        freq = defaultdict(int)
        freq[0]=1
        interestingCount = 0

        for i in range(n):
            if nums[i]%modulo==k:
                prefixSumSatisfyingNums = (prefixSumSatisfyingNums + 1) % modulo
            
            interestingCount += freq[(prefixSumSatisfyingNums - k +modulo)%modulo]

            freq[prefixSumSatisfyingNums]+=1

        return interestingCount