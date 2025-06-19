from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev, count = 0, 1
        
        for i in range(1,len(nums)):
            if nums[i]-nums[prev]>k:
                count+=1
                prev = i

        return count