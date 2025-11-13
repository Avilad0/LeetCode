# Bottom-Up Approach - DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
        m,n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    dp[i+1][j+1] = 1+dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[m][n]



# # Top-Down Approach - Memoization 
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
#         m,n = len(text1), len(text2)
#         memo = [[-1]*n for _ in range(m)]

#         def dfs(i, j):
#             if i==m or j==n:
#                 return 0
#             if memo[i][j]!=-1:
#                 return memo[i][j]

#             if text1[i]==text2[j]:
#                 maxLen = 1+dfs(i+1,j+1)
#             else:
#                 maxLen = max(dfs(i+1, j), dfs(i, j+1))

#             memo[i][j]=maxLen
#             return maxLen

#         return dfs(0,0)