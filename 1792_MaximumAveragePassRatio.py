from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        
        incRatioHeap = [((classes[i][0])/(classes[i][1]) - (classes[i][0]+1)/(classes[i][1]+1),i) for i in range(n)]
        heapq.heapify(incRatioHeap)
        
        for _ in range(extraStudents):
            __, i = heapq.heappop(incRatioHeap)

            classes[i][0]+=1
            classes[i][1]+=1

            heapq.heappush(incRatioHeap, ((classes[i][0])/(classes[i][1]) - (classes[i][0]+1)/(classes[i][1]+1),i))

        ans = 0
        for cls in classes:
            ans += (cls[0]/cls[1])

        return ans/n
        # return round(ans/n, 5)

# class Solution:
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
#         n = len(classes)
        
#         incRatioHeap = []
#         for i in range(n):
#             heapq.heappush(incRatioHeap, ((classes[i][0])/(classes[i][1]) - (classes[i][0]+1)/(classes[i][1]+1),i))
        
#         for _ in range(extraStudents):
#             __, i = heapq.heappop(incRatioHeap)

#             classes[i][0]+=1
#             classes[i][1]+=1

#             heapq.heappush(incRatioHeap, ((classes[i][0])/(classes[i][1]) - (classes[i][0]+1)/(classes[i][1]+1),i))

#         ans = 0
#         for cls in classes:
#             ans += (cls[0]/cls[1])

#         return round(ans/n, 5)
#         # return ans/n

'''

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
(3/4 + 3/5 + 2/2) / 3 = 0.78333


Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
((5/13) + (4/10) + (2/4) + (4/5)) / 4 = 0.5211538

'''