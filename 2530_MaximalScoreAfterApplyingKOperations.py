from typing import List
import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        score = 0

        for _ in range(k):
            score += heap[0]
            x = heapq.heappop(heap)
            heapq.heappush(heap, - math.ceil(-x/3))
        
        return -score