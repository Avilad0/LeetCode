from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS iterative, tc=O(n), sc=O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
                            
            curr = stack.pop()
            if k==1:
                return curr.val

            k-=1
            curr = curr.right
            
        return root.val


# # DFS recursive, tc=O(n), sc=O(n)
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         return self.kthSmallestRecur(root, k)[0]
    
#     def kthSmallestRecur(self, root, k):
#         if root == None:
#             return (None, k)
        
#         (kthSmall, currK) = self.kthSmallestRecur(root.left, k)

#         if kthSmall is not None:
#             return (kthSmall, currK)
        
#         if currK==1:
#             return (root.val, currK-1)
        
#         return self.kthSmallestRecur(root.right, currK-1)