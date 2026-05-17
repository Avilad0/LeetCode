from typing import List

# tc=O(n*(2^n)), sc = O(n)
# for tc, you have n-1 places you can choose to cut or not cut the array, and we explore all cuts. This is 2^n
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        ans = []
        stack = []

        def backtrack(i):
            if i==n:
                ans.append(stack[:])
                return 
            
            for j in range(i,n):                
                isPalindrome = True
                left, right=i, j
                while left<right:
                    if s[left]!=s[right]:
                        isPalindrome=False
                        break
                    left+=1
                    right-=1
                
                if isPalindrome:
                    stack.append(s[i:j+1])
                    backtrack(j+1)
                    stack.pop()

        backtrack(0)
        return ans