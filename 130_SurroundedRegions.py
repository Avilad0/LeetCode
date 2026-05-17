from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m,n = len(board), len(board[0])
        if m<3 or n<3:
            return

        dirs = ((0,1),(0,-1),(1,0),(-1,0))

        def markSafe(i,j):
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!="O":
                return
            
            board[i][j]="S"
            for (di, dj) in dirs:
                markSafe(i+di, j+dj)
                        

        for i in range(m):
            if board[i][0]=="O":
                markSafe(i,0)
            if board[i][n-1]=="O":
                markSafe(i,n-1)

        for j in range(n):
            if board[0][j]=="O":
                markSafe(0,j)
            if board[m-1][j]=="O":
                markSafe(m-1,j)            

        for i in range(m):
            for j in range(n):
                if board[i][j]=="S":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"
        

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         dirs = ((0,1),(0,-1),(1,0),(-1,0))

#         m,n = len(board), len(board[0])

#         def surroundable(i,j)->bool:
#             if i<0 or i>=m or j<0 or j>=n:
#                 return False
            
#             if not board[i][j] or board[i][j]=="X":
#                 return True
            
#             board[i][j]=None
#             for (di, dj) in dirs:
#                 if not surroundable(i+di, j+dj):
#                     return False

#             return True
        
#         def mark(i,j, c):
#             if i<0 or i>=m or j<0 or j>=n or board[i][j]:
#                 return
            
#             board[i][j]=c
#             for (di, dj) in dirs:
#                 mark(i+di, j+dj, c)
                

#         for i in range(m):
#             for j in range(n):
#                 if board[i][j]=="O":
#                     if surroundable(i,j):
#                         mark(i,j,"Y")
#                     else:
#                         mark(i,j,"N")
        

#         for i in range(m):
#             for j in range(n):
#                 if board[i][j]=="Y":
#                     board[i][j]="X"
#                 if board[i][j]=="N":
#                     board[i][j]="O"
        