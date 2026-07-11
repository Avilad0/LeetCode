from typing import List

# tc=O(n*(2^n)), sc = O(n^2)
# for tc, you have n-1 places you can choose to cut or not cut the array, and we explore all cuts. This is 2^n
# same concept as below but using dp to store valid palindromes to avoid duplicate checks for if the palindrome is valid
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)

        dp = [[False]*n for _ in range(n)]
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                dp[i][j] = s[i]==s[j] and (i+1>j-1 or dp[i+1][j-1])

        ans = []
        stack = []

        def backtrack(i):
            if i==n:
                ans.append(stack[:])
                return 
            
            for j in range(i,n):                                
                if dp[i][j]:
                    stack.append(s[i:j+1])
                    backtrack(j+1)
                    stack.pop()

        backtrack(0)
        return ans

# # tc=O(n*(2^n)), sc = O(n)
# # for tc, you have n-1 places you can choose to cut or not cut the array, and we explore all cuts. This is 2^n
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
        
#         n = len(s)
#         ans = []
#         stack = []

#         def backtrack(i):
#             if i==n:
#                 ans.append(stack[:])
#                 return 
            
#             for j in range(i,n):                
#                 isPalindrome = True
#                 left, right=i, j
#                 while left<right:
#                     if s[left]!=s[right]:
#                         isPalindrome=False
#                         break
#                     left+=1
#                     right-=1
                
#                 if isPalindrome:
#                     stack.append(s[i:j+1])
#                     backtrack(j+1)
#                     stack.pop()

#         backtrack(0)
#         return ans