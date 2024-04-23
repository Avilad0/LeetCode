from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        map = {i:[] for i in range(n) }
        degrees = [0] * n
        
        for u, v in edges:
            map[u].append(v)
            map[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        

        queue = deque([])
        for i in range(n):
            if degrees[i] == 1:
                queue.append(i)
        
        remaining = n
        while remaining > 2:
            size = len(queue)
            remaining -= size
            
            for i in range(size):
                leaf = queue.popleft()
                for neighbor in map[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        
        return list(queue)