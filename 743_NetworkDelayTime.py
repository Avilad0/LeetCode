from typing import List

import heapq

# tc=O(ElogV), sc=O(V+E)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = {i:[] for i in range(1,n+1)}
        for time in times:
            adjList[time[0]].append((time[1],time[2]))

        visited = set()
        heap = [(0,k)]
        while heap:
            (t, node) = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            if len(visited)==n:
                return t

            for (nxt, nxtT) in adjList[node]:
                if nxt not in visited:
                    heapq.heappush(heap, (t+nxtT, nxt))
        
        return -1