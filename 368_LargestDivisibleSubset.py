from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n=len(nums)
        prev = [(-1,1)]*n
        maxLen = 1
        maxLast = 0

        for i in range(1,n):

            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0 and prev[i][1]<prev[j][1]+1:
                    prev[i]=(j,prev[j][1]+1)

            if prev[i][1]>maxLen:
                maxLen = prev[i][1]
                maxLast = i

        ans = []
        while maxLast!=-1:
            ans.append(nums[maxLast])
            maxLast = prev[maxLast][0]
        return ans



# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
#         nums.sort()
#         n=len(nums)
#         memo = [[None]*n for _ in range(n)]

#         def backtrack(i, prev):
#             if i==n:
#                 return []
            
#             if prev!=-1 and memo[i][prev]!=None:
#                 return memo[i][prev]

#             maxSubset = backtrack(i+1, prev)
#             if prev == -1 or nums[i]%nums[prev]==0:
#                 temp = [nums[i]] + backtrack(i+1, i)
#                 if len(temp) > len(maxSubset):
#                     maxSubset = temp

#             memo[i][prev] = maxSubset
#             return maxSubset

#         return backtrack(0, -1)