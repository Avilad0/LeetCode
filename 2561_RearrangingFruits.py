from typing import List
from collections import defaultdict

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)

        freqDiff = defaultdict(int)

        for i in range(n):
            freqDiff[basket1[i]]+=1
            freqDiff[basket2[i]]-=1

        minNum = float('inf')
        totalSwapsNeeded = 0
        for k,v in freqDiff.items():
            if v%2:
                return -1
            totalSwapsNeeded+= abs(v)
            minNum = min(k, minNum)
        
        totalSwapsNeeded//=2

        minCost = 0
        sortedfreqDiff = sorted(list(freqDiff.items()), key= lambda x:x[0])
        freqIndex = 0
        while totalSwapsNeeded>0:
            swapsToDo = min(totalSwapsNeeded, abs(sortedfreqDiff[freqIndex][1]))

            minCost += min(sortedfreqDiff[freqIndex][0] * swapsToDo//2, minNum*swapsToDo)

            totalSwapsNeeded -= swapsToDo
            freqIndex+=1
        
        return minCost
    
print(Solution().minCost(basket1 = [4,2,2,2], basket2 = [1,4,1,2])) #1
print(Solution().minCost(basket1 = [84,80,43,8,80,88,43,14,100,88], basket2 = [32,32,42,68,68,100,42,84,14,8])) #48
print(Solution().minCost(basket1 = [4,4,4,4,3], basket2 = [5,5,5,5,3])) # 8