from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, queryN = len(nums), len(queries)
        
        heap = []
        deltaArray = [0]*(n+1)
        queries.sort(key = lambda x:x[0])

        currMaxRemoval, queryIndex =0, 0
        for i in range(n):
            currMaxRemoval+=deltaArray[i]

            while queryIndex<queryN and queries[queryIndex][0]==i:
                heapq.heappush(heap, -queries[queryIndex][1])
                queryIndex+=1
            
            while currMaxRemoval<nums[i] and heap and -heap[0]>=i:
                currMaxRemoval+=1
                maxIndexTobeRemoved = -heapq.heappop(heap)
                deltaArray[maxIndexTobeRemoved+1] -= 1
            
            if currMaxRemoval<nums[i]:
                return -1
        
        return len(heap)