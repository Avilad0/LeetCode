from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=1

        for i in range(1,n+1):
            for a in range(1,amount+1):
                # memo[(i,currAmount)] = dfs(i+1,currAmount) + dfs(i, currAmount+coins[i])
                dp[i][a] = dp[i-1][a] + (0 if a-coins[i-1]<0 else dp[i][a-coins[i-1]])
        
        return dp[n][amount]
    
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         memo = {}

#         def dfs(i, currAmount):
#             if currAmount==amount:
#                 return 1
            
#             if currAmount>amount or i>=n:
#                 return 0
            
#             if (i,currAmount) not in memo:
#                 memo[(i,currAmount)] = dfs(i+1,currAmount) + dfs(i, currAmount+coins[i])
            
#             return memo[(i,currAmount)]
        
#         return dfs(0,0)