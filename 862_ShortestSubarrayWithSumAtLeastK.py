from typing import List
from collections import heapq


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = float('inf')

        for i in 

    

# print(Solution().shortestSubarray(nums = [77,19,35,10,-14], k = 19))
print(Solution().shortestSubarray(nums = [84,-37,32,40,95], k = 167)) #3

# 84,47,79,119,214


# class Solution:
#     def shortestSubarray(self, nums: List[int], k: int) -> int:
#         ans = float('inf')
#         i,j,n = 0,0,len(nums)
#         summ = 0
        
#         while j<n and ans!=1:
#             summ+=nums[j]
#             if summ>=k:
#                 ans = min(ans, j-i+1)
#                 while i<j:
#                     summ-=nums[i]
#                     i+=1
#                     if summ>=k:
#                         ans=min(ans,j-i+1)
#                     else:
#                         break
#             j+=1

#         return -1 if ans==float('inf') else ans
    
