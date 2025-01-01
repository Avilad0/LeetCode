'''
ans = max(zeros_left+ones_right)
    = max(zeros_left + ones_total - ones_left)
    = max(zeros_left - ones_left) + ones_total
'''
# 1-pass
class Solution:
    def maxScore(self, s: str) -> int:
        ones_left, zeros_left, ans = 0, 0, -float('inf')
        for i in range(len(s)-1):
            if s[i]=='0':
                zeros_left+=1
            else:
                ones_left+=1
            
            if zeros_left-ones_left > ans:
                ans = zeros_left-ones_left
        
        if s[-1]=='1':
            ones_left+=1
        return ans + ones_left

# 2-Pass
# class Solution:
#     def maxScore(self, s: str) -> int:
#         n = len(s)
#         ones, zeros, ans = s.count('1'), 0, 0
#         for i in range(n-1):
#             if s[i]=='0':
#                 zeros+=1
#             else:
#                 ones-=1
            
#             if zeros+ones>ans:
#                 ans = zeros+ones
        
#         return ans

# good but more memory
# class Solution:
#     def maxScore(self, s: str) -> int:
#         n = len(s)
#         dp = [[0,0] for _ in range(n)]
#         if s[0]=='0':
#             dp[0][0] = 1 
#         if s[n-1]=='1':
#             dp[n-1][1] = 1
#         for i in range(1,n):
#             dp[i][0] = dp[i-1][0] + (1 if s[i]=='0' else 0)
#             dp[n-1-i][1] = dp[n-i][1] + (1 if s[n-1-i]=='1' else 0)

#         ans = dp[0][0]+dp[1][1]
#         for i in range(1,n-1):
#             if dp[i][0]+ dp[i+1][1] > ans:
#                 ans = dp[i][0]+dp[i+1][1]
#         return ans