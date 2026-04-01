"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodesSeen = {}

        def dfs(curr):
            if not curr: 
                return None
            if curr in nodesSeen:
                return nodesSeen[curr]
            
            newNode = Node(curr.val, [])
            nodesSeen[curr] = newNode

            for neighbor in curr.neighbors:
                newNode.neighbors.append(dfs(neighbor))

            return newNode
        
        return dfs(node)