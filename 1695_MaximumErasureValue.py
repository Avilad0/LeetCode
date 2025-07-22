from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n =len(nums)
        
        maxSum = nums[0]
        currSum = nums[0]

        uniqueNums = set([nums[0]])
        left = 0
        for right in range(1,n):
            while left<right and nums[right] in uniqueNums:
                uniqueNums.remove(nums[left])
                currSum-=nums[left]
                left+=1
            
            uniqueNums.add(nums[right])
            currSum+=nums[right]
            maxSum = max(maxSum, currSum)
        
        return maxSum