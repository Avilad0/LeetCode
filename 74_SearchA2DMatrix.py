from typing import List

# tc=O(log(mn)), sc=O(1) - binary search treating matrix as single array
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n =len(matrix), len(matrix[0])
        left, right = 0, m*n-1

        while left<=right:
            mid=(left+right)//2
            r,c = mid//n, mid%n
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                right=mid-1
            else:
                left=mid+1
        
        return False

# # tc=O(log(m)+log(n))=O(log(mn)), sc=O(1) - binary search with first row and then column search.
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         left, right = 0, len(matrix)-1
#         row = -1
#         while left<=right:
#             mid = (left+right)//2
#             if matrix[mid][0]<=target and target<=matrix[mid][-1]:
#                 row = mid
#                 break
#             elif matrix[mid][0]>target:
#                 right=mid-1
#             else:
#                 left=mid+1
        
#         if row!=-1:
#             left,right = 0, len(matrix[row])-1
#             while left<=right:
#                 mid = (left+right)//2
#                 if matrix[row][mid]==target:
#                     return True
#                 elif matrix[row][mid]>target:
#                     right=mid-1
#                 else:
#                     left=mid+1

#         return False