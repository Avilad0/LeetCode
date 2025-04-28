from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        greaterThanKSubarrays = 0

        left, currSum = 0, 0
        
        for right in range(n):
            currSum+=nums[right]
            while currSum*(right-left+1) >= k:
                greaterThanKSubarrays += (n-right)
                currSum-=nums[left]
                left+=1
        
        return (n*(n+1))//2  - greaterThanKSubarrays