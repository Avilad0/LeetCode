# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Since p and q are gauranteed to be present
# We just need to find node where p and q are on different sides and not on same side

# using BFS , tc: O(d) , sc: O(1)
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        while root:
            if max(p.val, q.val)<root.val:
                root = root.left
            elif min(p.val, q.val)>root.val:
                root = root.right
            else:        
                return root
        
        return root

# # using DFS , tc: O(d) , sc: O(d) 
 # class Solution:    
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
#         if max(p.val, q.val)<root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         if min(p.val, q.val)>root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
        
#         return root




# # find both p and q and return ancestor where both flags true

# # DFS
# class Solution:
#     def findAncestor(self, root, p, q):
#         if not root:
#             return (None, (False, False))

#         foundP, foundQ = False, False

#         if root==p:
#             foundP = True
#         elif root==q:
#             foundQ = True
        
#         if (not foundP and p.val<root.val) or (not foundQ and q.val<root.val):
#             (commonAncestor, (foundPInSubtree, foundQInSubtree)) = self.findAncestor(root.left, p, q)

#             foundP, foundQ = foundP or foundPInSubtree, foundQ or foundQInSubtree

#             if commonAncestor:
#                 return (commonAncestor, (foundPInSubtree, foundQInSubtree))

        
#         if (not foundP and p.val>root.val) or (not foundQ and q.val>root.val):
#             (commonAncestor, (foundPInSubtree, foundQInSubtree)) = self.findAncestor(root.right, p, q)

#             foundP, foundQ = foundP or foundPInSubtree, foundQ or foundQInSubtree

#             if commonAncestor:
#                 return (commonAncestor, (foundPInSubtree, foundQInSubtree))

        
#         if foundP and foundQ:
#             return (root, (foundP, foundQ))
        
#         return (None, (foundP, foundQ))
    
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         return self.findAncestor(root, p, q)[0]