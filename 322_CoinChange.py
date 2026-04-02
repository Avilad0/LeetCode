from typing import List

# same as below just removing minCoin variable, 
# tc=O(len(coin)*amount), sc=O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0]=0

        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
            
        return -1 if dp[amount]==amount+1 else dp[amount]


# 
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [0]*(amount+1)

#         for i in range(1,amount+1):
#             minCoin = float('inf')
#             for coin in coins:
#                 if i-coin>=0:
#                     minCoin = min(minCoin, dp[i-coin]+1)
            
#             dp[i] = minCoin
        
#         return -1 if dp[amount]==float('inf') else dp[amount]
