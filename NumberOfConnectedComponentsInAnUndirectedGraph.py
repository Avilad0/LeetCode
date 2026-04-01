from typing import List

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        self.components = n

    def find(self, u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])

        return self.parent[u]

    def union(self, u, v):
        pU, pV = self.find(u), self.find(v)

        if pU==pV:
            return
        
        self.components-=1
        self.parent[pV] = pU
        self.size[pU] += self.size[pV]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n)
        for u,v in edges:
            dsu.union(u,v)
            if dsu.components ==1:
                return 1
        
        return dsu.components
        