from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpsRemaining = 1
        for num in nums:
            if jumpsRemaining<=0:
                return False

            jumpsRemaining = max(jumpsRemaining-1, num)
        
        return True