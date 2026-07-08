class Solution:
    def numTilings(self, n: int) -> int:
        
        MOD = 10**9 + 7
        dp = [0]*(n+1)

        dp[0]=dp[1]=1

        for i in range(2,n+1):
            dp[i]= (2*dp[i-1] + (0 if i<3 else dp[i-3]) )%MOD

        return dp[n]

'''
dp[n] = dp[n-1] (|) +dp[n-2] (=) + 2*(dp[n-3]+dp[n-4]....+dp[0]) (|-____|)(|____-|)
dp[n] = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-3] + 2*(dp[n-4]...+dp[0])
dp[n] = dp[n-1] + dp[n-3] + (dp[n-2] + dp[n-3] + 2*(dp[n-4]...+dp[0]))
dp[n] = dp[n-1] + dp[n-3] + dp[n-1] (from above formula)
dp[n] = 2*dp[n-1]+dp[n-3]

'''

# class Solution:
#     def numTilings(self, n: int) -> int:
        
#         MOD = 10**9 + 7
#         dp = [[-1,-1] for _ in range(n+2)]

#         dp[n][0]=1
#         dp[n][1]= dp[n+1][0] = dp[n+1][1]=0

#         for i in range(n-1,-1,-1):
#             dp[i][0] = (dp[i+1][0] + 2*dp[i+1][1] + dp[i+2][0])%MOD
#             dp[i][1] = (dp[i+1][1] + dp[i+2][0])%MOD

#         return dp[0][0]

# class Solution:
#     def numTilings(self, n: int) -> int:
        
#         MOD = 10**9 + 7
#         memo = {}

#         def dfs(i, filled):
#             if i==n and filled==0:
#                 return 1
#             if i>=n:
#                 return 0

#             if (i,filled) in memo:
#                 return memo[(i,filled)]

#             ways = 0    
#             if filled ==0:
#                 ways = (dfs(i+1,0) + dfs(i+2,0) + 2*dfs(i+1,1))%MOD
#             else:
#                 ways = (dfs(i+1,1) + dfs(i+2,0))%MOD

#             memo[(i,filled)]= ways
#             return ways
#         return dfs(0, 0)
    


# class Solution:
#     def numTilings(self, n: int) -> int:
#         MOD = 10**9 + 7
#         dp = [[-1]*4 for _ in range(n+1)]

#         def dfs(i :int, tile1Available :bool, tile2Available :bool) -> int:

#             if i==n:
#                 return 1
            
#             currState = (1 if tile1Available else 0) | (2 if tile2Available else 0)

#             if dp[i][currState] != -1:
#                 return dp[i][currState]
            
#             tile3Available, tile4Available = i+1<n, i+1<n

#             ans = 0
            
#             # Adding Tromino
#             if tile1Available and tile2Available and tile3Available:
#                 ans += dfs(i+1, False, True)
#             if tile1Available and tile2Available and tile4Available:
#                 ans += dfs(i+1, True, False)
#             if tile1Available and (not tile2Available) and tile3Available and tile4Available:
#                 ans += dfs(i+1, False, False)
#             if (not tile1Available) and tile2Available and tile3Available and tile4Available:
#                 ans += dfs(i+1, False, False)
            
#             # Adding Domino    
#             if tile1Available and tile2Available:
#                 ans += dfs(i+1, True, True)
#             if tile1Available and tile2Available and tile3Available and tile4Available:
#                 ans += dfs(i+1, False, False)
#             if tile1Available and (not tile2Available) and tile3Available:
#                 ans += dfs(i+1, False, True)
#             if (not tile1Available) and tile2Available and tile4Available:
#                 ans += dfs(i+1, True, False)
            
#             # Both occupied till current
#             if (not tile1Available) and (not tile2Available):
#                 ans += dfs(i+1, True, True)

#             dp[i][currState] = ans%MOD
#             return dp[i][currState]

#         return dfs(0,True, True)