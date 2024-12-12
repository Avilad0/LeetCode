from typing import List
import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            x = heapq.heappop(gifts)
            x = math.floor(math.sqrt(-x))
            heapq.heappush(gifts, -x)

        return - sum(gifts)
    
print(Solution().pickGifts(gifts = [25,64,9,4,100], k = 4)) #29