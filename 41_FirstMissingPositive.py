from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        
        for i in range(l):
            if nums[i]<0:
                nums[i]=0

        for i in range(l):
            n = abs(nums[i])
            if n<=l and n>0:
                if nums[n-1]>0:
                   nums[n-1]*=-1
                elif nums[n-1]==0:
                    nums[n-1] = -1 * n
            
        
        i = 0
        while i<l and nums[i]<0:
            i+=1

        return i+1 


print(Solution().firstMissingPositive([3,4,0,2]))