from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        
        inc_count = 1
        dec_count = 1
        max_count = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc_count+=1
                if inc_count>max_count:
                    max_count = inc_count
            else:
                inc_count = 1

            if nums[i]<nums[i-1]:
                dec_count+=1
                if dec_count>max_count:
                    max_count = dec_count
            else:
                dec_count = 1

        return max_count
