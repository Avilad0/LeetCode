from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        decreasing_found = False
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                if decreasing_found:
                    return False
                decreasing_found=True
        
        if decreasing_found:
            return nums[0]>=nums[-1]

        return True