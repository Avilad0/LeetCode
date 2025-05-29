from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        n,m = len(edges1)+1, len(edges2)+1

        heights1 = self.getTargetNodes(n,edges1, True)
        
        heights2 = self.getTargetNodes(m,edges2, False)
        tree2NodesToAdd = max(len(heights2[0]), len(heights2[1]))

        targetNodes = [0]*n
        tree1EvenLen, tree1OddLen = len(heights1[0]) + tree2NodesToAdd, len(heights1[1]) + tree2NodesToAdd
        
        for node in heights1[0]:
            targetNodes[node] = tree1EvenLen

        for node in heights1[1]:
            targetNodes[node] = tree1OddLen

        return targetNodes

    
    def getTargetNodes(self, n, edges, isEvenStart) -> List[int]:
        adjList = [[] for _ in range(n)]
        
        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        
        heights = [[], []]
        currHeightIndex = 0 if isEvenStart else 1
        queue = deque([(0,-1)])
        
        while queue:
            currLen = len(queue)
            for _ in range(currLen):
                (curr, prev) = queue.popleft()
                heights[currHeightIndex].append(curr)
                for nxt in adjList[curr]:
                    if nxt != prev:
                        queue.append((nxt, curr))

            currHeightIndex ^=1
        
        return heights

    

'''
         0
    0           0
 1      2       3
4 5    6 7      8



'''