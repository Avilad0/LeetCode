from typing import List

# tc=O(n^2) , sc = O(n), n=9
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        horizontalSets = [0]*9
        verticalSets = [0]*9
        innerBoxSets = [0]*9

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue

                innerBoxIndex = 3*(i//3) + (j//3)
                currBit = 1<<(int(board[i][j])-1)
                
                if currBit & (horizontalSets[i] | verticalSets[j] | currBit&innerBoxSets[innerBoxIndex]):
                    return False
                else:
                    horizontalSets[i] |= currBit
                    verticalSets[j] |= currBit
                    innerBoxSets[innerBoxIndex] |= currBit

        return True

# # same as above only if condition is different for checking
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         horizontalSets = [0]*9
#         verticalSets = [0]*9
#         innerBoxSets = [0]*9

#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]==".":
#                     continue

#                 innerBoxIndex = 3*(i//3) + (j//3)
#                 currBit = 1<<(int(board[i][j])-1)
                
#                 if currBit&horizontalSets[i] or currBit&verticalSets[j] or currBit&innerBoxSets[innerBoxIndex]:
#                     return False
#                 else:
#                     horizontalSets[i] |= currBit
#                     verticalSets[j] |= currBit
#                     innerBoxSets[innerBoxIndex] |= currBit

#         return True
    

# tc=O(n^2) , sc = O(n^2), n=9
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         horizontalSets = [set() for _ in range(9)]
#         verticalSets = [set() for _ in range(9)]
#         innerBoxSets = [set() for _ in range(9)]

#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]==".":
#                     continue

#                 innerBoxIndex = 3*(i//3) + (j//3)
                
#                 if board[i][j] in horizontalSets[i] or board[i][j] in verticalSets[j] or board[i][j] in innerBoxSets[innerBoxIndex]:
#                     return False
#                 else:
#                     horizontalSets[i].add(board[i][j])
#                     verticalSets[j].add(board[i][j])
#                     innerBoxSets[innerBoxIndex].add(board[i][j])

#         return True


# tc=O(n^2) , sc = O(n^2), n=9
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         #validate horizontal
#         #validate vertical
#         for i in range(9):
#             numsHorizontal = set()
#             numsVertical = set()
#             for j in range(9):
#                 if (board[i][j]=="." or board[i][j] not in numsHorizontal) and (board[j][i]=="." or board[j][i] not in numsVertical):
#                     numsHorizontal.add(board[i][j])
#                     numsVertical.add(board[j][i])
#                 else:
#                     return False

#         #validate 3x3 boxes
#             for sI in [0,3,6]:
#                 for sJ in [0,3,6]:
#                     nums = set()
#                     for i in range(sI, sI+3):
#                         for j in range(sJ, sJ+3):
#                             if board[i][j]=="." or board[i][j] not in nums:
#                                 nums.add(board[i][j])
#                             else:
#                                 return False

#         return True