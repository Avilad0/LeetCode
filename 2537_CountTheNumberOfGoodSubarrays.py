from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n, goodCount, currPairs = len(nums), 0, 0
        
        freq = {}
        left=0
        for right in range(n):
            if nums[right] in freq:
                currPairs+=freq[nums[right]]
                freq[nums[right]]+=1
            else :
                freq[nums[right]]=1
            
            while currPairs>=k and left<right:
                goodCount += n-right
                freq[nums[left]]-=1
                currPairs -= freq[nums[left]]
                left+=1
        
        return goodCount