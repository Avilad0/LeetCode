from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        for i in range(2):
            for j in range(3):
                if board[i][j]==0:
                    break
        
        queuee = deque([board, i, j, 0])

        while queuee:
            b = queuee.

        
        return -1