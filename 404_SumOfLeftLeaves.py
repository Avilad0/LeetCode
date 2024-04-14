from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.runningLeftLeavesSum(root, False)
    

    def runningLeftLeavesSum(self, root: Optional[TreeNode], isLeft: bool) -> int:
        
        if root ==None:
            return 0

        if root.left==None and root.right==None and isLeft:
            return root.val
        
        return self.runningLeftLeavesSum(root.left, True) + self.runningLeftLeavesSum(root.right, False)
    