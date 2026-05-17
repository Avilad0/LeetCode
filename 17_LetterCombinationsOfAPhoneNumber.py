from typing import List

# tc=O(n*(4^n)), sc=O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n<1:
            return []
            
        mp = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv", "9":"wxyz"}
        
        ans = []
        stack = []

        def backtrack(i):
            if i==n:
                ans.append("".join(stack))
                return

            for c in mp[digits[i]]:
                stack.append(c)
                backtrack(i+1)
                stack.pop()

        backtrack(0)
        return ans