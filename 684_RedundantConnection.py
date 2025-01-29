from typing import List

class DisjointSet:
    def __init__(self,n):
        self.n = n
        self.parent = [i for i in range(n+1)]
        self.size = [1]*(n+1)
    
    def getParent(self, node) -> int:
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.getParent(self.parent[node])
        return self.parent[node]


    def unionBySize(self, u, v):
        u = self.getParent(u)
        v = self.getParent(v)

        if u==v:
            return False
        
        if self.size[u] < self.size[v]:
            self.parent[u] = v
            self.size[v]+=self.size[u]
        else:
            self.parent[v] = u
            self.size[u]+=self.size[v]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjointSet = DisjointSet(len(edges))

        for e in edges:
            if not disjointSet.unionBySize(e[0],e[1]):
                return e
        
        return None