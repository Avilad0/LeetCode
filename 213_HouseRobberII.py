from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]

        ans = 0
        for start in range(2):
            prevPrevHouse, prevHouse = 0, 0
            for i in range(start,n-1+start):
                prevPrevHouse, prevHouse = prevHouse, max(nums[i] + prevPrevHouse, prevHouse)
                
            ans = max(ans, prevHouse)

        return ans