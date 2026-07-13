from typing import List

# # tc = O(n+m), sc = O(m), m=max start value of all intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        maxVal = max(start for start,end in intervals)
        mp = [-1]*(maxVal+1)

        for start,end in intervals:
            mp[start]=max(mp[start], end)    

        ans=[]
        start, end=None, None
        for i in range(maxVal+1):
            if mp[i]!=-1:
                if start is None:
                    start = i
                    end = mp[i]
                else:
                    end=  max(end, mp[i])
            if i==end or i==maxVal:
                ans.append([start,end])
                start,end=None,None

        return ans

# # tc = O(nlogn), sc = O(n)
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         ans = []
#         for interval in intervals:
#             if not ans or ans[-1][1]<interval[0]:
#                 ans.append(interval)
#             else:
#                 ans[-1][1] = max(ans[-1][1], interval[1])

#         return ans