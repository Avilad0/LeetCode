from typing import List
from collections import deque

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adjList1 = self.getAdjList(edges1)
        adjList2 = self.getAdjList(edges2)

        diameter1 = self.getDiameter(adjList1)
        diameter2 = self.getDiameter(adjList2)

        return max( diameter1, diameter2, (diameter1+1)//2 + (diameter2+1)//2 + 1)

        
    def getAdjList(self, edges: List[List[int]]) -> List[List[int]]:
        adjList = [[] for _ in range(len(edges)+1)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        return adjList
    
    def getDiameter(self, adjList: List[List[int]]) -> int:
        _, farthestNode = self.bfsLen(adjList, 0)
        diameter, _ = self.bfsLen(adjList, farthestNode)
        return diameter
    
    def bfsLen(self, adjList: List[List[int]], node: int):
        queue = deque([node])
        diameter, farthestNode = 0, node
        visited = [False]*len(adjList)
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                visited[curr] = True
                for x in adjList[curr]:
                    if not visited[x]:
                        queue.append(x)
                
            if queue:
                diameter+=1
                farthestNode = queue[-1]

        return diameter, farthestNode
