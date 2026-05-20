from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        start, end = n-1, 0
        currGas = gas[start]-cost[start]
        while start>end:
            if  currGas<0:
                start-=1
                currGas+=gas[start]-cost[start]
            else:
                currGas+=gas[end]-cost[end]
                end+=1
        return start if currGas>=0 else -1

# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         if sum(cost)>sum(gas):
#             return -1
        
#         n=len(gas)
#         start = 0
#         currGas = 0
#         for i in range(n):
#             currGas+=gas[i]-cost[i]
#             if currGas<0:
#                 currGas=0
#                 start=i+1
        
#         return start