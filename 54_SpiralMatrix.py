# Using loops for 4 directions
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m,n = len(matrix), len(matrix[0])

        top, bottom, left, right = 0,m-1, 0, n-1

        ans = []

        while top<=bottom and left<=right:

            for col in range(left, right+1):
                ans.append(matrix[top][col])
            top+=1

            for row in range(top, bottom+1):
                ans.append(matrix[row][right])
            right-=1

            if top>bottom or left>right:
                break

            for col in range(right, left-1, -1):
                ans.append(matrix[bottom][col])
            bottom-=1

            for row in range(bottom, top-1, -1):
                ans.append(matrix[row][left])
            left+=1

        return ans


# Using direction indexes
# from typing import List

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

#         m,n = len(matrix), len(matrix[0])

#         dirs = [(0,1),(1,0),(0,-1),(-1,0)]
#         dirsIndex=0

#         row,col = 0,0
#         rowMin, rowMax, colMin, colMax = 1,m-1, 0, n-1

#         ans = []

#         for _ in range(m*n):
#             ans.append(matrix[row][col])

#             if dirsIndex==0:
#                 if col == colMax:
#                     dirsIndex=1
#                     colMax-=1
#             elif dirsIndex==1:
#                 if row == rowMax:
#                     dirsIndex=2
#                     rowMax-=1
#             elif dirsIndex==2:
#                 if col == colMin:
#                     dirsIndex=3
#                     colMin+=1
#             elif dirsIndex==3:
#                 if row == rowMin:
#                     dirsIndex=0
#                     rowMin+=1
            
#             row+=dirs[dirsIndex][0]
#             col+=dirs[dirsIndex][1]
                

#         return ans