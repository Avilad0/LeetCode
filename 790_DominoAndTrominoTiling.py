class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[-1]*4 for _ in range(n+1)]

        def dfs(i :int, tile1Available :bool, tile2Available :bool) -> int:

            if i==n:
                return 1
            
            currState = (1 if tile1Available else 0) | (2 if tile2Available else 0)

            if dp[i][currState] != -1:
                return dp[i][currState]
            
            tile3Available, tile4Available = i+1<n, i+1<n

            ans = 0
            
            # Adding Tromino
            if tile1Available and tile2Available and tile3Available:
                ans += dfs(i+1, False, True)
            if tile1Available and tile2Available and tile4Available:
                ans += dfs(i+1, True, False)
            if tile1Available and (not tile2Available) and tile3Available and tile4Available:
                ans += dfs(i+1, False, False)
            if (not tile1Available) and tile2Available and tile3Available and tile4Available:
                ans += dfs(i+1, False, False)
            
            # Adding Domino    
            if tile1Available and tile2Available:
                ans += dfs(i+1, True, True)
            if tile1Available and tile2Available and tile3Available and tile4Available:
                ans += dfs(i+1, False, False)
            if tile1Available and (not tile2Available) and tile3Available:
                ans += dfs(i+1, False, True)
            if (not tile1Available) and tile2Available and tile4Available:
                ans += dfs(i+1, True, False)
            
            # Both occupied till current
            if (not tile1Available) and (not tile2Available):
                ans += dfs(i+1, True, True)

            dp[i][currState] = ans%MOD
            return dp[i][currState]

        return dfs(0,True, True)