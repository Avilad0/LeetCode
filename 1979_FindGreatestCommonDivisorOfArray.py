from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minI, maxI = -1, -1
        for i in range(len(nums)):
            if minI==-1 or nums[i]<nums[minI]:
                minI = i
            if maxI == -1 or nums[i]>nums[maxI]:
                maxI=i

        a,b = nums[maxI], nums[minI]

        while b>0:
            a, b = b, a%b
        
        return a