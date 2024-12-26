from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        if abs(target)>totalSum:
            return 0
        dp = [[0]*(totalSum*2 + 1) for _ in range(n)]
        dp[0][totalSum+nums[0]] = 1
        dp[0][totalSum-nums[0]] += 1


        for i in range(1,n):
            for summ in range(-totalSum, totalSum+1):
                if dp[i-1][summ+totalSum]>0:
                    dp[i][summ+totalSum+nums[i]] +=dp[i-1][summ+totalSum]
                    dp[i][summ+totalSum-nums[i]] +=dp[i-1][summ+totalSum]

        return dp[n-1][target+totalSum]

# TLE in python but will work in C++/Java, O(2**n)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n, totalWays = len(nums), 0
#         def dfs(i,summ) :
#             if i==n:
#                 if summ==target:
#                     nonlocal totalWays
#                     totalWays+=1
#                 return
            
#             dfs(i+1, summ+nums[i])
#             dfs(i+1, summ-nums[i])
        
#         dfs(0,0)
#         return totalWays