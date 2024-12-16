from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        numsHeap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(numsHeap)
        for _ in range(k):
            __, i = heapq.heappop(numsHeap)
            nums[i] *=multiplier
            heapq.heappush(numsHeap, (nums[i], i))

        return nums