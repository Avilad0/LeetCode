from typing import List

# Bottom-Up DP - Tabulation
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        freq = []
        wordLen, targetLen = len(words[0]), len(target)

        for i in range(wordLen):
            freq.append([0]*26)
            for word in words:
                freq[i][ord(word[i])-97]+=1

        dp = [[-1]*(targetLen+1) for _ in range(wordLen+1)]
        for j in range(targetLen):
            dp[wordLen][j] = 0

        for i in range(wordLen+1):
            dp[i][targetLen] = 1

        for minWordIndex in range(wordLen-1, -1, -1):
            for targetIndex in range(targetLen-1, -1, -1):
                dp[minWordIndex][targetIndex] = dp[minWordIndex+1][targetIndex]
                
                targetChar = ord(target[targetIndex])-97
                if freq[minWordIndex][targetChar]:
                    dp[minWordIndex][targetIndex] = (dp[minWordIndex][targetIndex] + (freq[minWordIndex][targetChar]*dp[minWordIndex+1][targetIndex+1])%MOD)%MOD
        
        return dp[0][0]
    

# # Top-Down DP - Memoization
# class Solution:
#     def numWays(self, words: List[str], target: str) -> int:
#         MOD = 10**9 + 7
#         freq = []
#         wordLen, targetLen = len(words[0]), len(target)

#         for i in range(wordLen):
#             freq.append([0]*26)
#             for word in words:
#                 freq[i][ord(word[i])-97]+=1

#         memo = [[-1]*targetLen for _ in range(wordLen)]
#         def dfs(minWordIndex: int, targetIndex: int):
#             if targetLen == targetIndex:
#                 return 1
            
#             if minWordIndex == wordLen:
#                 return 0
            
#             if memo[minWordIndex][targetIndex] != -1:
#                 return memo[minWordIndex][targetIndex]
            
#             # without using current index
#             ways = dfs(minWordIndex+1, targetIndex) 
            
#             #with using current minIndex
#             targetChar = ord(target[targetIndex])-97
#             if freq[minWordIndex][targetChar]:
#                 ways = (ways + (freq[minWordIndex][targetChar]*dfs(minWordIndex+1, targetIndex+1))%MOD)%MOD
            
#             memo[minWordIndex][targetIndex] = ways

#             return ways
        
#         return dfs(0, 0)