from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        length = len(nums)
        n = length//3

        currMinSum = 0
        firstHalfHeap = []
        for i in range(n):
            currMinSum+=nums[i]
            heapq.heappush(firstHalfHeap, -nums[i])
        

        prefixMinimumSum = [currMinSum]
        for i in range(n, 2*n):
            heapq.heappush(firstHalfHeap, -nums[i])
            removedNum = -heapq.heappop(firstHalfHeap)
            currMinSum = currMinSum +nums[i] - removedNum
            prefixMinimumSum.append(currMinSum)
        

        currMaxSum = 0
        secondHalfHeap = []
        for i in range(3*n -1, 2*n -1 ,-1):
            currMaxSum+=nums[i]
            heapq.heappush(secondHalfHeap, nums[i])


        minDiff = prefixMinimumSum[n] - currMaxSum
        for i in range(2*n-1, n-1, -1):
            heapq.heappush(secondHalfHeap, nums[i])
            removedNum = heapq.heappop(secondHalfHeap)
            currMaxSum = currMaxSum + nums[i] - removedNum
            minDiff = min(minDiff, prefixMinimumSum[i-n]-currMaxSum)

        
        return minDiff