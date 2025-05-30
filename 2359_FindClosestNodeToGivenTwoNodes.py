from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        visited = [[False]*n for _ in range(2)]

        queue = deque([(node1,0),(node2,1)])
        ans = []
        while (not ans) and queue:
            currN = len(queue)

            for _ in range(currN):
                (curr,fromNode) = queue.popleft()
                
                visited[fromNode][curr] = True

                if visited[fromNode^1][curr]:
                    ans.append(curr)
                
                if edges[curr]!=-1 and (not visited[fromNode][edges[curr]]):
                    queue.append((edges[curr], fromNode))
        
        if not ans:
            return -1
        
        return min(ans)