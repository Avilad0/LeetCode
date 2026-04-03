from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left, right = 0, n-1        

        while left<right:
            for i in range(right-left):
                top, bottom = left, right

                temp = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = temp


# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """

#         n = len(matrix)
#         for i in range(n//2):
#             for j in range(i,n-i-1):
#                 curr = matrix[i][j]
#                 matrix[i][j] = matrix[n-1-j][i]
#                 matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
#                 matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
#                 matrix[j][n-1-i] = curr


# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n= len(matrix)
#         for i in range(n):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
#         for i in range(n):
#             for j in range(n//2):
#                 matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]