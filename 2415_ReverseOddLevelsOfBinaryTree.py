from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# better space complexity
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse( left_node: TreeNode , right_node: TreeNode, level):
            if not left_node:
                return            
            if level:
                left_node.val, right_node.val = right_node.val, left_node.val
            
            traverse(left_node.left, right_node.right, level^1)
            traverse(left_node.right, right_node.left, level^1)

        traverse(root.left, root.right, 1)
        return root

# class Solution:
#     def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         queue = [root]
#         level, maxNodes = 0, 1
#         while True:
#             if level:
#                 for i in range(maxNodes//2):
#                     queue[i].val, queue[maxNodes-1-i].val = queue[maxNodes-1-i].val, queue[i].val

#             if queue[0].left==None:
#                 break
#             for _ in range(maxNodes):
#                 queue.append(queue[0].left)
#                 queue.append(queue[0].right)
#                 queue.pop(0)
                
        
#             level^=1
#             maxNodes*=2

#         return root