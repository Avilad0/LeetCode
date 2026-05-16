# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isValid = True
        def dfs(node):
            nonlocal isValid
            if not node or not isValid:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left-right)>1:
                isValid=False
                return 0
            
            return max(left, right)+1
        
        dfs(root)
        return isValid