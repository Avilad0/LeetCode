from typing import List

# DP + Binary Search,  tc= O(nlogn) , sc= O(n)
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # for increasing subsequence of len i, dp[i-1] = min( last num in subsequence of len i) 
        dp = [] 
        dp.append(nums[0])

        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
            else:
                idx = bisect_left(dp, nums[i])
                dp[idx] = nums[i]

        return len(dp)

# 1D DP , tc= O(n^2) , sc= O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n

        for i in range(n-1):
            for j in range(i+1, n):
                if nums[j]>nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)
        
        return dp[n-1]




# # 2D DP - Memory Limit Error , tc= O(n^2) , sc= O(n^2)
# import sys
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         sys.setrecursionlimit(9999999) 

#         n = len(nums)
#         memo = {}

#         def dfs(curr, prev):
#             if curr == n:
#                 return 0
#             if (curr, prev) in memo:
#                 return memo[(curr, prev)]

#             ans = dfs(curr+1, prev)
#             if prev==-1 or nums[curr]>nums[prev]:
#                 ans = max(ans, 1 + dfs(curr+1, curr))
            
#             memo[(curr,prev)]=ans
#             return ans
        
#         return dfs(0,-1)