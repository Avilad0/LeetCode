from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return root
        
        if root.left:
            root.left  = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)

        if root.left==None and root.right==None and root.val==target:
            return None
        
        return root