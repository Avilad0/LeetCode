from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum,count = 0,0
        for i in range(len(nums)-1):
            left_sum+=nums[i]
            right_sum-=nums[i]
            if left_sum>=right_sum:
                count+=1
        return count
