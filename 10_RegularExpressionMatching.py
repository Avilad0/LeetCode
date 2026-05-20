class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n=len(s), len(p)

        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[m][n]=True

        for i in range(m,-1,-1):
            for j in range(n-1,-1,-1):
                isChMatch = i<m and (p[j]=="." or p[j]==s[i])
                if j+1<n and p[j+1]=="*":
                    dp[i][j] = dp[i][j+2] or (isChMatch and dp[i+1][j])
                elif isChMatch:
                    dp[i][j] = dp[i+1][j+1]

        return dp[0][0]
    

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m, n=len(s), len(p)

#         memo = {}
#         def backtrack(i,j):
#             if i==m and j==n:
#                 return True
#             if j==n:
#                 return False
            
#             if (i,j) not in memo:
#                 if j+1<n and p[j+1]=="*":
#                     memo[(i,j)] = backtrack(i,j+2) or (i<m and (p[j]=="." or p[j]==s[i]) and (backtrack(i+1,j)))
#                 elif i<m and (p[j]=="." or p[j]==s[i]):
#                     memo[(i,j)] =  backtrack(i+1,j+1)
#                 else:
#                     memo[(i,j)] = False

#             return memo[(i,j)]
#         return backtrack(0,0)