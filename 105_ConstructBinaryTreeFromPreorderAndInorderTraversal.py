from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS optimized with index params and hashmap, tc: O(n), sc: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderMap = { inorder[i]:i for i in range(len(inorder))}

        def buildTreeRecur(pStart, pEnd, iStart, iEnd) -> Optional[TreeNode]:
            print(pStart, pEnd, iStart, iEnd)
            if pStart>pEnd:
                return None

            root = TreeNode(preorder[pStart])

            if pStart!=pEnd:
                rootIndexInInorder = inorderMap[preorder[pStart]] #also the number of elements on left subtree
                root.left = buildTreeRecur(pStart+1 , pStart + (rootIndexInInorder-iStart), iStart, rootIndexInInorder-1)
                root.right = buildTreeRecur(pStart + (rootIndexInInorder-iStart) + 1, pEnd, rootIndexInInorder+1, iEnd)

            return root
    
        return buildTreeRecur(0, len(preorder)-1, 0, len(inorder)-1)


# # DFS, tc: O(n^2), sc: O(n^2)
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
#         if not preorder:
#             return None

#         root = TreeNode(preorder[0])
#         rootIndexInInorder = inorder.index(preorder[0]) #also the number of elements on left subtree
#         root.left = self.buildTree(preorder[1:1+rootIndexInInorder], inorder[:rootIndexInInorder])
#         root.right = self.buildTree(preorder[1+rootIndexInInorder:], inorder[rootIndexInInorder+1:])

#         return root