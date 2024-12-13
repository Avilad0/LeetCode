from typing import List
import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n=len(nums)
        marked = [False]*n
        score =0 
        numsHeap = []
        for i,num in enumerate(nums):
            heapq.heappush(numsHeap, (num,i))

        for _ in range(n):
            num,i = heapq.heappop(numsHeap)
            if marked[i]:
                continue
            
            score+=num
            marked[i]=True
            if i>0:
                marked[i-1]=True
            if i<n-1:
                marked[i+1]=True
        
        return score