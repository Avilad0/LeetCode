from typing import List

#tc=O(n), sc=O(1) - 2D DP - Tabulation - space optimized
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp = [[0,0] for _ in range(n+2)]    #[i][0]=buying, [i][1]=selling
        dp_1_0=dp_2_0=0
        dp_1_1=0


        for i in range(n-1,-1,-1):
            #buying at i
            # memo[(i,buying)] = max( dfs(i+1, False) - prices[i], dfs(i+1, True))
            # dp[i][0] = max(dp[i+1][1]-prices[i], dp[i+1][0])

            #selling at i
            #memo[(i,buying)] = max( prices[i] + dfs(i+2, True), dfs(i+1, False))
            # dp[i][1] = max(prices[i]+dp[i+2][0], dp[i+1][1])

            #use first
            new_dp_1_0 = max(dp_1_1-prices[i], dp_1_0)
            new_dp_1_1 = max(prices[i]+dp_2_0, dp_1_1)

            #update later
            dp_1_0, dp_2_0 = new_dp_1_0,dp_1_0
            dp_1_1 = new_dp_1_1


        return dp_1_0

# #tc=O(n), sc=O(n) - 2D DP - Tabulation 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         dp = [[0,0] for _ in range(n+2)]    #[i][0]=buying, [i][1]=selling

#         for i in range(n-1,-1,-1):
#             #buying at i
#             # memo[(i,buying)] = max( dfs(i+1, False) - prices[i], dfs(i+1, True))
#             dp[i][0] = max(dp[i+1][1]-prices[i], dp[i+1][0])

#             #selling at i
#             #memo[(i,buying)] = max( prices[i] + dfs(i+2, True), dfs(i+1, False))
#             dp[i][1] = max(prices[i]+dp[i+2][0], dp[i+1][1])

#         return dp[0][0]

# #tc=O(n), sc=O(n) - 2D DP - Memoization 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)

#         memo = {}
#         def dfs(i, buying):
#             # print(i,buyI)
#             if i>=n:
#                 return 0
            
#             if (i,buying) not in memo:
#                 if buying:
#                     memo[(i,buying)] = max( dfs(i+1, False) - prices[i], dfs(i+1, True))
#                 else:
#                     memo[(i,buying)] = max( prices[i] + dfs(i+2, True), dfs(i+1, False))
            
#             return memo[(i,buying)]

#         return dfs(0,True)