from collections import defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        adjList = [set() for _ in range(n)]
        roots = set([i for i in range(n)])

        for e1, e2 in edges:
            if e1 in adjList[e2]:
                return -1
            
            adjList[e1].add(e2)
            if e2 in roots:
                roots.remove(e2)
        
        visited = [False]*n
        dp = {}
        def dfs(node):
            if visited[node]:
                return -1
            
            if node in dp:
                return dp[node]
            
            visited[node] = True
            currFreq = defaultdict(int)

            for child in adjList[node]:
                childFreq = dfs(child)
                if childFreq == -1:
                    return childFreq
                
                for c, f in childFreq.items():
                    currFreq[c] = max(f, currFreq[c])

            currFreq[colors[node]]+=1

            visited[node] = False
            dp[node] = currFreq

            return dp[node]
        

        largestPathVal = -1
        for root in roots:
            f = dfs(root)
            if f == -1:
                return -1
            
            for c, f in f.items():
                largestPathVal = max(largestPathVal, f)
        
        return largestPathVal