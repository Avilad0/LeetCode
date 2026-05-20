from typing import List

# tc=O(n), sc = O(1) - Greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        
        left = right = 0
        currJumps = 0

        while left<=right<n-1:
            currJumps+=1
            maxReach = right
            for i in range(left, right+1):
                maxReach = max(i+nums[i], maxReach)
            
            left, right = right+1, maxReach


        return currJumps if right>=n-1 else -1

# # tc=O(n^2), sc = O(n) - dp
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n=len(nums)
#         dp = [float('inf') for _ in range(n)]
#         dp[0]=0
#         for i in range(n):
#             for j in range(i+1, min(n, i+1+nums[i])):
#                 dp[j] = min(dp[j],1+dp[i])
        
#         return dp[n-1]