from typing import List
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        freq = defaultdict(int)
        n, uniques, right = len(nums), len(set(nums)), 0
        ans =0

        for left in range(n):
            if left>0:
                removeNum = nums[left-1]
                freq[removeNum]-=1
                if freq[removeNum]==0:
                    freq.pop(removeNum)
            
            while right<n and len(freq) < uniques:
                addNum = nums[right]
                freq[addNum] +=1
                right+=1
            
            if len(freq) == uniques:
                ans += n - right + 1

        return ans