from typing import List
from collections import deque

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

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        disjointSet = DisjointSet(n)
        adjList = [[] for _ in range(n+1)]
        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])
            disjointSet.unionByRank(e[0],e[1])

        maxGroupsInCluster = {}
        for node in range(1,n+1):
            numberOfGroups = self.findNumberOfGroupsFromNode(n, adjList, node)
            if numberOfGroups == -1:
                return -1
            
            parentNode = disjointSet.getParent(node)
            if (parentNode not in maxGroupsInCluster) or (maxGroupsInCluster[parentNode]<numberOfGroups):
                maxGroupsInCluster[parentNode] = numberOfGroups
        
        return sum(maxGroupsInCluster.values())


    def findNumberOfGroupsFromNode(self, n: int, adjList :List[List[int]], start: int) -> int:

        groups = [-1]*(n+1)
        groups[start] = 1
        nextGroup = 2

        queue = deque([start])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in adjList[node]:
                    if groups[neighbor] == -1:
                        groups[neighbor] = nextGroup
                        queue.append(neighbor)
                    elif groups[neighbor] == nextGroup-1:
                        return -1
            nextGroup+=1
            
        return nextGroup - 2

    


print(Solution().magnificentSets(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))    # Output: 4
print(Solution().magnificentSets(92,[[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]]))    # Output: 57
