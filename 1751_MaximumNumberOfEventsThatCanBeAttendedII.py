from typing import List
from bisect import bisect_left, bisect_right

# Bottom-Up DP with Cached-Binary Search , tc = O(n*k)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)

        nextIndexes = [bisect_right(events, events[i][1], i+1, key = lambda x:x[0]) for i in range(n)]

        dp = [[-1]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=0
        
        for j in range(k+1):
            dp[n][j]=0
        
        for j in range(1, k+1):
            for i in range(n-1, -1, -1):
                val = dp[i+1][j]

                val = max(val, events[i][2] + dp[nextIndexes[i]][j-1])

                dp[i][j] =  val
        
        return dp[0][k]
    


# # Bottom-Up DP with Binary Search, tc = O(n*k*log(n))
# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         events.sort()
#         n = len(events)

#         dp = [[-1]*(k+1) for _ in range(n+1)]
#         for i in range(n+1):
#             dp[i][0]=0
        
#         for j in range(k+1):
#             dp[n][j]=0
        
#         for j in range(1, k+1):
#             for i in range(n-1, -1, -1):
#                 val = dp[i+1][j]

#                 nextIndex = bisect_left(events, events[i][1]+1, i+1, key = lambda x:x[0])
#                 val = max(val, events[i][2] + dp[nextIndex][j-1])

#                 dp[i][j] =  val
        
#         return dp[0][k]
    

# # Top-down DP with Binary Search
# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         events.sort()
#         n = len(events)

#         memo = {}
        
#         def dfs(index, remainingK):
#             if index == n or remainingK==0:
#                 return 0
            
#             if (index, remainingK) in memo:
#                 return memo[(index, remainingK)]
            
#             # without using curr index
#             val = dfs(index+1, remainingK)

#             # with using current index
#             nextIndex = bisect_left(events, events[index][1]+1, index+1, key = lambda x:x[0])
#             val = max(val, events[index][2] + dfs(nextIndex, remainingK-1))

            
#             memo[(index, remainingK)] = val
#             return val
    
#         return dfs(0,k)