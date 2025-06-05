class DisjointSet:
    def __init__(self,n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [26-i for i in range(n)]
    
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

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        ds = DisjointSet(26)

        for i in range(len(s1)):
            ds.unionByRank(ord(s1[i])-97, ord(s2[i])-97)

        smallest = list(baseStr)
        for i in range(len(smallest)):
            smallest[i] = chr(97 + ds.getParent(ord(smallest[i])-97))

        return "".join(smallest)
    

print(Solution().smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))  #aauaaaaada