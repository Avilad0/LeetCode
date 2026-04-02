# DP Bottom-up tabular space optimized, tc= O(n), sc= O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return n

        steps0, steps1 = 1,1

        for i in range(2,n+1):
            steps0, steps1 = steps1, steps1+steps0
        
        return steps1


# # DP Bottom-up tabular, tc= O(n), sc= O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n==0 or n==1:
#             return n

#         steps = [0]*(n+1)
#         steps[0]=steps[1]=1

#         for i in range(2,n+1):
#             steps[i]=steps[i-1]+steps[i-2]
        
#         return steps[n]


# # Top-down DP recursion : tc= O(n), sc= O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         cache = {}
#         def dp(i):
#             if i<0:
#                 return 0
#             if i<2:
#                 return 1

#             if i in cache:
#                 return cache[i]
            
#             cache[i]=dp(i-1)+dp(i-2)
#             return cache[i]
        
#         return dp(n)