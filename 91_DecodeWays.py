class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0 or s[0]=='0':
            return 0
        if n==1:
            return 1

        # dp = [0]*(n+1)
        # dp[0] = dp[1] = 1
        dp0 = dp1 = 1
        for i in range(1,n):
            if s[i]=='0':
                if s[i-1]!='1' and s[i-1]!='2':
                    return 0
                # dp[i+1] = dp[i-1]
                dp0, dp1 = dp1, dp0
            elif s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6'):
                # dp[i+1] = dp[i] + dp[i-1]
                dp0, dp1 = dp1, dp1+dp0
            else:
                # dp[i+1] = dp[i]
                dp0, dp1 = dp1, dp1


        return dp1




# # DP , tc = O(n) , sc = O(n)
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         if n==0 or s[0]=='0':
#             return 0
#         if n==1:
#             return 1

#         dp = [0]*(n+1)
#         dp[0] = dp[1] = 1

#         for i in range(1,n):
#             if s[i]=='0':
#                 if s[i-1]!='1' and s[i-1]!='2':
#                     return 0
#                 dp[i+1] = dp[i-1]

#             elif s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6'):
#                     dp[i+1] = dp[i] + dp[i-1]
#             else:
#                 dp[i+1] = dp[i]

#         return dp[n]


'''
      - 2 6 1 1 0 5 5 9 7 1 7 5 6 5 6 2"
dp = [1 1 2 2 4 2 2 2 2 2 2 4 4 4 4 4 4 ]
'''