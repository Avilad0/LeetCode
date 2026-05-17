from typing import List

# tc = O(Cn * n)    (where Cn is catalan number for n = (1/(n+1)) * (2n)C(n) =(approximately) (4^n)/(n^(3/2)) )
# tc=O((4^n)/sqrt(n)), sc=O(n)
# the tc is related to catalan number.
# although we can also say tc is (2n)C(n) as choosing n opening brackets in 2n positions.
# but that number is bigger than the quoted tc as it also considers invalid choices like puting opening brackets in end
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        stack = []
        def backtrack(openN, closeN):
            if openN==n and closeN==n:
                ans.append("".join(stack))
                return

            if openN<n:
                stack.append('(')
                backtrack(openN+1, closeN)
                stack.pop()
            
            if closeN<openN:
                stack.append(')')
                backtrack(openN, closeN+1)
                stack.pop()
        
        backtrack(0,0)
        return ans