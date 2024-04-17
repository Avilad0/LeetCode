from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = "z"*31
        def traverse(node: Optional[TreeNode], s : str):
            
            if node == None:
                return

            s = chr(node.val + 97) + s

            if node.left==None and node.right==None:
                nonlocal ans
                ans = min(ans, s)
            
            traverse(node.left ,s)
            traverse(node.right,s)
        
        traverse(root, "")
        return ans
    

print(Solution().smallestFromLeaf(TreeNode(0,None, TreeNode(1))))