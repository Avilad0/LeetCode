from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if num-1 not in numsSet:
                currLen = 1
                while num+currLen in numsSet:
                    currLen+=1
                longest = max(currLen, longest)
        
        return longest