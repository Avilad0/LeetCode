from typing import List

# Min-Heap
# tc = O(nlogn + qlogq + nlogn) = O(nlogn + qlogq),  sc=O(n+q) , n=len(intervals), q=len(queries)
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n= len(intervals)

        intervals.sort()
        
        qRes = {}
        
        i = 0
        mh = []
        for q in sorted(queries):
            while i<n and intervals[i][0]<=q:
                heapq.heappush(mh, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i+=1

            while mh and mh[0][1]<q:
                heapq.heappop(mh)   #do pop after pushing as those intervals recently pushed might even be ending before the q starts.

            
            if mh:
                qRes[q]=mh[0][0]
            else:
                qRes[q]=-1

        return [qRes[q] for q in queries]

# # TLE
# # tc = O(n*maxIntervalSize) 
# class Solution:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
#         n= len(intervals)

#         maxEnd = max(end for start,end in intervals)
#         minIntervals = [-1]*(maxEnd+1)

#         for start,end in intervals:
#             l = end-start+1
#             for i in range(start, end+1):
#                 if minIntervals[i]==-1 or minIntervals[i]>l:
#                     minIntervals[i] = l
        
#         ans = []
#         for q in queries:
#             if q>maxEnd:
#                 ans.append(-1)
#             else:
#                 ans.append(minIntervals[q])
        
#         return ans