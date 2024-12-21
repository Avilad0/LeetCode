from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        connections = [[] for _ in range(n)]
        for e in edges:
            connections[e[0]].append(e[1])
            connections[e[1]].append(e[0])

        visited = [False]*n
        components = 0
        def dfs(node) -> int:
            if visited[node]:
                return 0
            visited[node] = True
            
            child_remainder = 0
            for c in connections[node]:
                if not visited[c]:
                    child_remainder += dfs(c)
            
            if (child_remainder + values[node])%k==0:
                nonlocal components
                components += 1
                return 0
            
            return child_remainder + values[node]         

        dfs(0)
        return components   
    

print(Solution().maxKDivisibleComponents(n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6)) #2
print(Solution().maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3)) #3
