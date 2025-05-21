from typing import List

# tc = O(2mn), sc = O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        isFirstColZero = False

        for i in range(m):
            if matrix[i][0]==0:
                isFirstColZero = True

            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(m-1, -1,-1):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            
            if isFirstColZero:
                matrix[i][0]=0

# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[0,1,2,0],[3,4,5,2],[0,3,1,0]]
Solution().setZeroes(matrix)
print(matrix)

# # tc = O(3mn), sc = O(m+n)
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m,n = len(matrix), len(matrix[0])

#         rows, cols = set(), set()

#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]==0:
#                     rows.add(i)
#                     cols.add(j)
        
#         for i in rows:
#             for j in range(n):
#                 matrix[i][j]=0

#         for j in cols:
#             for i in range(m):
#                 matrix[i][j]=0