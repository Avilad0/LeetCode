from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum, run_sum = nums[0], nums[0]

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                run_sum += nums[i]
            else:
                if max_sum<run_sum:
                    max_sum = run_sum
                run_sum = nums[i]

        return max_sum if max_sum>run_sum else run_sum
        

print(Solution().maxAscendingSum([10,20,30,5,10,50]))   #65