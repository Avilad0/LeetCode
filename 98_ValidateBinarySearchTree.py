from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidSubBST(root, -float('inf'), float('inf'))

    def isValidSubBST(self, root, minVal, maxVal) -> bool:
        if not root:
            return True
        
        isValid = True
        if root.left:
            if minVal<root.left.val<root.val:
                isValid = isValid and self.isValidSubBST(root.left, minVal, root.val)
            else:
                return False
        
        if isValid and root.right:
            if root.val<root.right.val<maxVal:
                isValid = isValid and self.isValidSubBST(root.right, root.val, maxVal)
            else:
                return False
        
        return isValid