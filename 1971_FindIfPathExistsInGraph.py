from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        map={i:[] for i in range(n)}

        for e in edges:
            map[e[0]].append(e[1])
            map[e[1]].append(e[0])
        
        stack=[source]
        
        while stack:
            v=stack.pop(0)
            if v==destination:
                return True
            if v in map:
                stack.extend(map.pop(v))
            
        return False
