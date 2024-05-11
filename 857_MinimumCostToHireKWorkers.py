import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        n = len(wage)

        wage_per_quality = [(wage[i]/quality[i], quality[i]) for i in range(n)]
        wage_per_quality.sort(key=lambda i:i[0])

        ans = float('inf')
        running_quality_count = 0
        highest_quality_list = []

        for i in range(n):
            heapq.heappush(highest_quality_list, -wage_per_quality[i][1])
            running_quality_count += wage_per_quality[i][1]

            if len(highest_quality_list) > k:
                running_quality_count += heapq.heappop(highest_quality_list)

            if len(highest_quality_list) == k:
                ans = min(ans, running_quality_count * wage_per_quality[i][0])

        return ans

print(Solution().mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2))
print(Solution().mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3))
print(Solution().mincostToHireWorkers(quality = [1,2], wage = [14,16], k = 1))