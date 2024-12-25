from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#DFS
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node:TreeNode, level:int):
            if not node:
                return
            
            if len(ans)==level:
                ans.append(node.val)
            else:
                ans[level] = max(ans[level], node.val)
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        return ans

#BFS
# class Solution:
#     def largestValues(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         queue = deque([root])
#         ans = []
#         while queue:
#             maxx = -float('inf')
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if maxx<node.val:
#                     maxx = node.val
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             ans.append(maxx)
        
#         return ans