from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        n = len(pairs)

        adjList = defaultdict(list)
        outgoingDegree, incomingDegree = defaultdict(int), defaultdict(int)
        for i in range(n):
            start, end = pairs[i]
            adjList[start].append(end)
            outgoingDegree[start]+=1
            incomingDegree[end]+=1
        
        startNode = -1
        for node in outgoingDegree:
            if outgoingDegree[node]>incomingDegree[node]:
                startNode = node
                break
        
        if startNode == -1:
            startNode = pairs[0][0]
        
        ans = []
        def visit(node):
            while adjList[node]:
                nextNode = adjList[node].pop()
                visit(nextNode)
            ans.append(node)

        visit(startNode)

        ans.reverse()

        return [[ans[i-1],ans[i]] for i in range(1,len(ans))]