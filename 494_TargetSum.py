from typing import List

from collections import defaultdict

# Same concept as below but using dict to eliminate unnecessary sums.
# tc=O(n*m), sc=O(m), m=sum of all nums
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)

        dp = defaultdict(int)
        dp[nums[0]]+=1
        dp[-nums[0]]+=1

        for i in range(1,n):
            newDp = defaultdict(int)
            for j in dp.keys():
                newDp[j-nums[i]] += dp[j]
                newDp[j+nums[i]] += dp[j]
            
            dp=newDp

        return dp[target]

# # Same concept as below but using dict to eliminate unnecessary sums.
# # tc=O(n*m), sc=O(n*m), m=sum of all nums
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n=len(nums)

#         dp = [defaultdict(int) for _ in range(n)]
#         dp[0][nums[0]]+=1
#         dp[0][-nums[0]]+=1

#         for i in range(1,n):
#             for j in dp[i-1].keys():
#                 dp[i][j-nums[i]] += dp[i-1][j]
#                 dp[i][j+nums[i]] += dp[i-1][j]
#             # print(dp)

#         return dp[n-1][target]


# tc=O(n*m), sc=O(n*m), m=sum of all nums
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         totalSum = sum(nums)
#         if abs(target)>totalSum:
#             return 0
#         dp = [[0]*(totalSum*2 + 1) for _ in range(n)]
#         dp[0][totalSum+nums[0]] = 1
#         dp[0][totalSum-nums[0]] += 1


#         for i in range(1,n):
#             for summ in range(-totalSum, totalSum+1):
#                 if dp[i-1][summ+totalSum]>0:
#                     dp[i][summ+totalSum+nums[i]] +=dp[i-1][summ+totalSum]
#                     dp[i][summ+totalSum-nums[i]] +=dp[i-1][summ+totalSum]

#         return dp[n-1][target+totalSum]