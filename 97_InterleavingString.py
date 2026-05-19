class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n = len(s1), len(s2)
        if m+n!=len(s3):
            return False
        
        if m<n:
            s1,s2=s2,s1
            m,n=n,m

        dp = [False]*(n+1)
        dp[n]=True
        
        for i in range(m,-1,-1):
            nextDp = [False]*(n+1)
            if i==m:
                nextDp[n]=True
            for j in range(n,-1,-1):
                if (i<m and s1[i]==s3[i+j] and dp[j]) or (j<n and s2[j]==s3[i+j] and nextDp[j+1]):
                    nextDp[j] = True

            dp = nextDp

        return dp[0]
    

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m,n = len(s1), len(s2)
#         if m+n!=len(s3):
#             return False

#         dp = [[False]*(n+1) for _ in range(m+1)]
#         dp[m][n]=True
        
#         for i in range(m,-1,-1):
#             for j in range(n,-1,-1):
#                 if (i<m and s1[i]==s3[i+j] and dp[i+1][j]) or (j<n and s2[j]==s3[i+j] and dp[i][j+1]):
#                     dp[i][j] = True
        
#         return dp[0][0]

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m,n = len(s1), len(s2)
#         if m+n!=len(s3):
#             return False

#         memo = {}
#         def backtrack(i,j):
#             if i==m and j==n:
#                 return True
            
#             if (i,j) not in memo:
#                 memo[(i,j)] = (i<m and s1[i]==s3[i+j] and backtrack(i+1,j)) or (j<n and s2[j]==s3[i+j] and backtrack(i,j+1))

#             return memo[(i,j)]
        
#         return backtrack(0,0)