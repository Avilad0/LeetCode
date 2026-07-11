"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

#BFS, samt complexity as below
# tc = O(V+E), sc=O(V)
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val,[])
        q = deque([node])

        while q:        
            old = q.popleft()
            new = oldToNew[old]
            for neighbor in old.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                new.neighbors.append(oldToNew[neighbor])

        
        return oldToNew[node]

# DFS
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         nodesSeen = {}

#         def dfs(curr):
#             if not curr: 
#                 return None
#             if curr in nodesSeen:
#                 return nodesSeen[curr]
            
#             newNode = Node(curr.val, [])
#             nodesSeen[curr] = newNode

#             for neighbor in curr.neighbors:
#                 newNode.neighbors.append(dfs(neighbor))

#             return newNode
        
#         return dfs(node)