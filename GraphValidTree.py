from typing import List

# DFS (detect cycles): tc: O(V+E) = O(n), sc: O(V+E) = O(n)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        adjList = [[] for _ in range(n)]
        for v0, v1 in edges:
            adjList[v0].append(v1)
            adjList[v1].append(v0)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for nxt in adjList[node]:
                if nxt!=prev and not dfs(nxt, node):
                    return False
        
            return True
        
        isAcyclic = dfs(0,-1)

        return isAcyclic and len(visited)==n
    

# # Disjoint Set Union (path compression): tc: O(V + E*alpha(V)) = O(n+ n*alpha(n)), sc: O(V) = O(n)
# class DSU:
#     def __init__(self,n):
#         self.parent = [i for i in range(n)]
#         self.size = [1]*n
#         # self.components = n

#     def getParent(self, u):
#         if self.parent[u]!=u:
#             self.parent[u] = self.getParent(self.parent[u])
#         return self.parent[u]

#     def add(self, u, v) -> bool:
#         pU, pV = self.getParent(u), self.getParent(v)

#         if pU == pV:
#             return False

#         # we don't need to check which one is bigger since any node can be root of tree and we don't have any use for it.
#         self.parent[pV]=pU
#         self.size[pU]+=self.size[pV]
#         # self.components-=1
#         return True

# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:

#         if len(edges) != n-1:
#             return False

#         dsu = DSU(n)

#         for u,v in edges:
#             if not dsu.add(u,v):
#                 return False
        
#         # we don't need components because if there are only n-1 edges in acyclic graph of n nodes, all nodes will be connected
#         # return self.components==1 
#         return True
