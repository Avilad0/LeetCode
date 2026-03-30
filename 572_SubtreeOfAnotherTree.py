from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Prefix tranverse and subtring finding,  tc: O(m+n), sc: O(m+n)
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False
        
        rootString = self.getPrefixString(root)
        subRootString = self.getPrefixString(subRoot)

        return subRootString in rootString
    
    def getPrefixString(self, root) -> str:
        
        if not root:
            return "$#"

        return "$" + str(root.val) + self.getPrefixString(root.left) + self.getPrefixString(root.right)


# # DFS - tree matching approach,  tc: O(m*n), sc: O(max(d_m, d_n))
# class Solution:   
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
#         if not root:
#             return False
        
#         if root.val == subRoot.val:
#             isSubtreeFound = self.isTreeEqual(root, subRoot)
#             if isSubtreeFound:
#                 return True

#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
#     def isTreeEqual(self, root1, root2):
#         if not root1 and not root2:
#             return True
        
#         if root1 and root2 and root1.val==root2.val:
#             return self.isTreeEqual(root1.left, root2.left) and self.isTreeEqual(root1.right, root2.right)
        
#         return False