from functools import cache
from typing import List

# Iterative, tc = O(n), sc=O(1)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        n = len(nums)

        onlyOddLen = nums[0]&1
        
        oddEvenLen = 1
        currBit = nums[0]&1
        
        for i in range(1, len(nums)):
            if nums[i]&1:
                onlyOddLen+=1

            if nums[i]&1!=currBit:
                oddEvenLen+=1
                currBit^=1

        return max(onlyOddLen, n-onlyOddLen, oddEvenLen) 



# # DFS, tc = O(4n), sc = O(4n)
# class Solution:
#     def maximumLength(self, nums: List[int]) -> int:
#         n = len(nums)

#         @cache
#         def dfs(index, prevBit, modSum):
#             if index==n:
#                 return 0
            
#             l = dfs(index+1, prevBit, modSum)
            
#             if (nums[index]+prevBit)%2==modSum:
#                 l=max(l, 1+dfs(index+1, nums[index]&1, modSum))
            
#             return l
        
#         return max(dfs(0,0,0), dfs(0,0,1), dfs(0,1,0), dfs(0,1,1))