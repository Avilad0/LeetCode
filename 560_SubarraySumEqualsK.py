from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        prefixSumMap = {0:1}

        currSum = 0
        for num in nums:
            currSum += num
            
            if currSum-k in prefixSumMap:
                count+=prefixSumMap[currSum-k]
            
            prefixSumMap[currSum] = prefixSumMap.get(currSum,0)+1

        return count