from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        events = []
        for i in intervals:
            events.append([i[0],1])
            events.append([i[1]+1,-1])

        events.sort(key = lambda x: (x[0],x[1]))

        max_concurrent = 0
        concurrent = 0

        for event in events:
            concurrent += event[1]
            if concurrent>max_concurrent:
                max_concurrent=concurrent
        
        return max_concurrent



'''

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

[1,5]
    [1,10]
        [2,3]
        [5,10]
[6,8]

'''