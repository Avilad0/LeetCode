from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def getRootToLeafNumbers(node : Optional[TreeNode], prefix: int): 
            
            if node == None:
                return 
            
            t= prefix*10 + node.val
            
            if node.left == None and node.right==None:
                nonlocal ans
                ans+=t
            
            getRootToLeafNumbers(node.left, t)     
            getRootToLeafNumbers(node.right, t)
        
        getRootToLeafNumbers(root,0)
        return ans
    
print(Solution().sumNumbers(TreeNode(1, TreeNode(1))))