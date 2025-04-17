from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n, count = len(nums),0
        indexDict = defaultdict(list)

        for i in range(n):
            for index in indexDict[nums[i]]:
                if (index*i)%k==0:
                    count+=1
            
            indexDict[nums[i]].append(i)
            
        return count


# class Solution:
#     def countPairs(self, nums: List[int], k: int) -> int:
#         n, count = len(nums),0

#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i]==nums[j] and (i*j)%k==0:
#                     count+=1
        
#         return count