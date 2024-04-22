from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if '0000' in deadends:
            return -1
        
        queue = deque([('0000', 0)])
        visited = set(['0000'] + deadends)
        
        while queue:
            current_combination, moves = queue.popleft()

            if current_combination == target:
                return moves
            
            for i in range(4):
                for delta in [-1, 1]:
                    new_combination = current_combination[:i] + str(((int(current_combination[i]) + delta) % 10)) + current_combination[i+1:]
                    
                    if new_combination not in visited:
                        visited.add(new_combination)
                        queue.append((new_combination, moves + 1))
        
        return -1