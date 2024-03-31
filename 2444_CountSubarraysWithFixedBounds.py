from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans =0
        minIndex, maxIndex,s = -1, -1,-1

        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                s=i
            
            if nums[i]==minK:
                minIndex=i
            if nums[i]==maxK:
                maxIndex=i
            
            t = min(maxIndex,minIndex) - s
            if t>0:
                ans+=t
        return ans


print(Solution().countSubarrays([1,3,5,2,7,5], 1,5))
print(Solution().countSubarrays([1,1,1,1], 1,1))

