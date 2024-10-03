from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        target = sum(nums) % p
        if target==0:
            return 0
        
        n = len(nums)
        mapOfMods = {0:-1}
        minLength = n
        runningSum = 0

        for i in range(n):
            runningSum= (runningSum + nums[i])%p
            toFind = (runningSum - target + p)%p
            
            if toFind in mapOfMods and i-mapOfMods[toFind] < minLength:
                minLength = i-mapOfMods[toFind]

            mapOfMods[runningSum] = i

        if minLength==n:
            return -1
        return minLength 

        # n=len(nums)
        # mods = [nums[0]%p]
        # setMods = set([mods[0]])
        # for i in range(1,n):
        #     mods.append((mods[i-1]+nums[i])%p)
        #     setMods.add(mods[i])

        # if mods[n-1]==0:
        #     return 0

        # if mods[n-1] in setMods:
        #     return 1
        
        # for s in range(2,p):
        #     for i in range(s-1, n):
                