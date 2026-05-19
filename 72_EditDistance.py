class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)

        memo = {}
        def backtrack(i,j):
            if j==n:
                return m-i
            
            if i==m:
                return n-j
            
            if (i,j) not in memo:
                if word1[i]==word2[j]:
                    memo[(i,j)] = backtrack(i+1,j+1)
                else:
                    memo[(i,j)] = 1+min(backtrack(i,j+1), backtrack(i+1,j), backtrack(i+1,j+1))

            return memo[(i,j)]

        return backtrack(0,0)