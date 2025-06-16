from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff, minNum = -1,float('inf')

        for num in nums:
            if num<minNum:
                minNum = num
            elif num>minNum:
                if maxDiff< num-minNum:
                    maxDiff = num-minNum
        
        return maxDiff