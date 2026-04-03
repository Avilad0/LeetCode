from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x:x[1])
        rem = 0
        last = -float('inf')
        for interval in intervals:
            if interval[0]>=last:
                last = interval[1]
            else:
                rem+=1
        
        return rem