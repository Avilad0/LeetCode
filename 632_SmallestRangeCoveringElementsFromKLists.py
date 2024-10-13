from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        numsLength = len(nums)
        numLengths = [len(_) for _ in nums]
        heap = []
        maxx = -100002
        for i in range(numsLength):
            heapq.heappush(heap, [nums[i][0],i,0])
            if nums[i][0] > maxx:
                maxx = nums[i][0]
    
        smallest_range_min = heap[0][0] 
        smallest_range_max = maxx
        
        while True:
            top = heapq.heappop(heap)
            if top[2] == numLengths[top[1]]-1 or smallest_range_max==smallest_range_min:
                return [smallest_range_min, smallest_range_max]
            top[2]+=1
            top[0]=nums[top[1]][top[2]]

            if top[0]>maxx:
                maxx = top[0]
            
            heapq.heappush(heap, top)

            if maxx-heap[0][0] < smallest_range_max-smallest_range_min:
                smallest_range_min,smallest_range_max = heap[0][0], maxx

        return []
            





# TLE on 87/90 test case
# class Solution:
#     def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
#         smallest_range = [0,100002]
#         numsLength = len(nums)
#         indexes=[0]*numsLength
#         numLengths = [ len(x) for x in nums]
        
#         while True:
#             minn = 100002
#             minnIndex = -1
#             maxx = 0
#             for i in range(numsLength):
#                 if indexes[i] == numLengths[i]:
#                     return smallest_range
                
#                 if nums[i][indexes[i]] < minn:
#                     minn = nums[i][indexes[i]]
#                     minnIndex = i
#                 if nums[i][indexes[i]] > maxx:
#                     maxx = nums[i][indexes[i]]
            
#             if maxx-minn < smallest_range[1] - smallest_range[0]:
#                 smallest_range = [minn,maxx]

#             indexes[minnIndex] +=1
        
#         return smallest_range