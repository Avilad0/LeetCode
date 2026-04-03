from typing import List

# tc = O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)
        ans = []
        i = 0

        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1
        
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        
        ans.append(newInterval)

        while i<n:
            ans.append(intervals[i])
            i+=1

        return ans 
    

# tc = O(n + logn)
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

#         n = len(intervals)

#         left, right = 0,n-1
#         while left<=right:
#             mid = (left+right)//2
#             if newInterval[0] > intervals[mid][0]:
#                 left = mid+1
#             else:
#                 right = mid-1

#         intervals.insert(left, newInterval)
        
#         i=1
#         while i<len(intervals):
#             if intervals[i][0]>intervals[i-1][1]:
#                 i+=1
#             else :
#                 intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
#                 intervals.pop(i)
        
#         return intervals