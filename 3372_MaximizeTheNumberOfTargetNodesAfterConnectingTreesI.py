from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        n,m = len(edges1)+1, len(edges2)+1

        adjList1 = [[] for _ in range(n)]
        adjList2 = [[] for _ in range(m)]

        for e1, e2 in edges1:
            adjList1[e1].append(e2)
            adjList1[e2].append(e1)

        for e1, e2 in edges2:
            adjList2[e1].append(e2)
            adjList2[e2].append(e1)



        targetNodes1 = self.getTargetNodes(n,adjList1, k)
        
        if k==0:
            return targetNodes1
        elif k==1:
            maxTargetValueTree2 = 1
        else:
            maxTargetValueTree2 = max(self.getTargetNodes(m,adjList2, k-1))

        for i in range(n):
            targetNodes1[i] += maxTargetValueTree2
        
        return targetNodes1

    
    def getTargetNodes(self, n, adjList, k) -> List[int]:
        targetNodes = []
        for i in range(n):
            targetNodes.append(self.dfs(i,-1, adjList, k))
        
        return targetNodes
    
    def dfs(self, curr, prev, adjList, k):
        if k==0:
            return 1

        targetNodes = 1
        for nxt in adjList[curr]:
            if nxt!=prev:
                targetNodes += self.dfs(nxt, curr, adjList, k-1)
        
        return targetNodes