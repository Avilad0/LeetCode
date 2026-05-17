from typing import List

#tc=O(n!), sc=O(n^2) - same as below but constant isSafe operation using hashset
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans = []
        board = [["."]*n for _ in range(n)]
        cols = set()
        leftDiag = set()    # row+col will be constant for leftDiag, eg: (0,5),(1,4),(2,3)....
        rightDiag = set()   # row-col will be constant for rightDiag, eg: (0,5),(1,6),(2,7)....

        def backtrack(row):
            if row==n:
                ans.append(["".join(br) for br in board])
                return

            for col in range(n):
                if col not in cols and (row+col) not in leftDiag and (row-col) not in rightDiag:
                    cols.add(col)
                    leftDiag.add(row+col)
                    rightDiag.add(row-col)
                    
                    board[row][col]="Q"
                    backtrack(row+1)
                    board[row][col]="."

                    cols.remove(col)
                    leftDiag.remove(row+col)
                    rightDiag.remove(row-col)
                    

        backtrack(0)
        return ans


# #tc=O(n!), sc=O(n^2) - same as above but O(n) isSafe operation
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
        
#         ans = []
#         board = [["."]*n for _ in range(n)]

#         def isSafe(row, col):
#             for i in range(1,row+1):
#                 if board[row-i][col]!="." or ( col-i>=0 and board[row-i][col-i]!=".") or ( col+i<n and board[row-i][col+i]!="."):
#                     return False

#             return True 

#         def backtrack(row):
#             if row==n:
#                 ans.append(["".join(br) for br in board])
#                 return

#             for col in range(n):
#                 if isSafe(row, col):
#                     board[row][col]="Q"
#                     backtrack(row+1)
#                     board[row][col]="."


#         backtrack(0)
#         return ans