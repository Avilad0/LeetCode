from typing import List

class Solution:
    m,n=0,0
    matrixx = None
    def countSquares(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrixx = matrix
        
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                ans += self.count(i,j,1)

        return ans


    def count(self, i:int, j:int, depth:int) -> int:
        if i>=self.m or j>=self.n or self.matrixx[i][j]==0:
            return 0

        self.matrixx[]


'''
size 
1 = 1
2 = 1 + 4 (size(1))
3 = 1 + 4 (size(2)) + 9 (size(1))
4 = 1 + 4 (size(3)) + 9 (size(2)) + 16 (size(1))
.
.
.

1111
1111
1111
1111
'''