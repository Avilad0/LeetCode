from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        dir = 0

        for i in range(1,n):
            if nums[i]>nums[i-1] and dir!=1:
                count+=1
                dir = 1
            elif nums[i]<nums[i-1] and dir!=-1:
                count+=1
                dir = -1
        
        return count - (0 if dir==0 else 1)