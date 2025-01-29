class DisjointSet:
    def __init__(self,n):
        self.n = n
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
    
    def getParent(self, node) -> int:
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.getParent(self.parent[node])
        return self.parent[node]


    def unionByRank(self, u, v):
        u = self.getParent(u)
        v = self.getParent(v)

        if u==v:
            return
        
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[v] < self.rank[u]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u]+=1