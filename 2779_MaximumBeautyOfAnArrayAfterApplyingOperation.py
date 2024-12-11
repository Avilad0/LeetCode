from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right=0,0
        n = len(nums)
        k=2*k
        ans = 0
        while right<n:
            while right<n and nums[right]-nums[left]<=k:
                right+=1
            
            ans = max(ans, right-left)
            left+=1

        return ans