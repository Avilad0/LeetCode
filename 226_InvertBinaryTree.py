from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# n = no. of nodes, d = depth of tree, w = max-width of tree
# if a complete binary tree: 
#   2^d <= n <= 2^(d+1) -1, d = floor(log2(n))
#   2^(d-1) <= w <= 2**d      (for d >= 1)

# DFS - tc:O(n) , sc:O(d)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    

# # BFS - tc:O(n) , sc:O(w)
# from collections import deque

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         if not root:
#             return None

#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             node.left, node.right = node.right, node.left
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#         return root