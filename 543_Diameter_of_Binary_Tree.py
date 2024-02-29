from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeNodeWithDepth(TreeNode):
    def __init__(self, val=0, left=None, right=None, depth=0):
        super().__init__(val, left, right)
        self.depth=depth


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dTree: TreeNodeWithDepth = root
        return traverse(root,0)
    
    def traverse(node, length:int)->int:
        if node==None:
            return 1
        

        traverse(node.left)