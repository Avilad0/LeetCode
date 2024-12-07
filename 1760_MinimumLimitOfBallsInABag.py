from typing import List
import math

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)
        while left<right:
            mid = (left+right)//2
            if self.isPossibleDivision(nums, maxOperations, mid):
                right = mid
            else:
                left = mid+1
        
        return left
    
    def isPossibleDivision(self, nums, maxOperation, maxNum):
        currentOperations = 0
        for n in nums:
            currentOperations+= math.ceil(n/maxNum) - 1
        
        return currentOperations<=maxOperation

print(Solution().minimumSize(nums = [9], maxOperations = 2))    #3