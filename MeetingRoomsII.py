from typing import List
"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Using Line-Sweep : tc=O(nlogn), sc=O(n)
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        line = defaultdict(int)
        for interval in intervals:
            line[interval.start]+=1
            line[interval.end]-=1
        
        currMeetings = 0
        ans = 0
        for i in sorted(line.keys()):
            currMeetings+=line[i]
            ans = max(ans, currMeetings)


        return ans

# # Using Heap : tc=O(nlogn), sc=O(n)
# import heapq
# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         heap = []
#         intervals.sort(key = lambda x:x.start)
#         ans = 0

#         for interval in intervals:
#             while heap and interval.start>=heap[0]:
#                 heapq.heappop(heap)
            
#             heapq.heappush(heap, interval.end)
#             ans = max(ans, len(heap))

#         return ans