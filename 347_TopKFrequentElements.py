from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k== len(nums):
            return nums
            
        freqMap = {}

        for num in nums:
            freqMap[num]=freqMap.get(num,0) + 1

        heap = []
        for (key,val) in freqMap.items():
            heapq.heappush(heap, (val,key))
            if len(heap)>k:
                heapq.heappop(heap)

        ans = [key for (val,key) in heap]

        return ans