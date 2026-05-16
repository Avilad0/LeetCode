from typing import List
import heapq

# tc= O(nlogn), sc=O(n) - using maxHeap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            x,y= -heapq.heappop(heap), -heapq.heappop(heap)
            newS = abs(x-y)
            if newS>0:
                heapq.heappush(heap, -newS)
        
        return 0 if len(heap)==0 else -heap[0]
    

# tc= O(n + max(stones)), sc=O(max(stones)) - using bucket sort
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxS = max(stones)
        freq = [0]*(maxS+1)

        for stone in stones:
            freq[stone]+=1
        
        i = maxS
        while i>=0:
            x = i
            freq[i]-=1
            while i>=0 and freq[i]==0:
                i-=1
            
            if i<0:
                return x

            y=i
            freq[i]-=1

            newS = abs(x-y)
            if newS>0:
                freq[newS]+=1

            i=x
            while i>=0 and freq[i]==0:
                i-=1

        return 0