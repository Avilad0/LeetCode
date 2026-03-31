from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Optimized DFS (refactored max functions, same complexity) -  tc: O(n), sc: O(d)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float('inf')

        def maxPathSumRecur(node):
            if not node:
                return 0
            
            leftSubtreeSum = max(0, maxPathSumRecur(node.left)) 
            rightSubtreeSum = max(0, maxPathSumRecur(node.right))

            nonlocal maxSum
            maxSum = max(maxSum, node.val + leftSubtreeSum + rightSubtreeSum)

            return node.val + max(leftSubtreeSum, rightSubtreeSum)
        
        maxPathSumRecur(root)

        return maxSum
    
# Optimized DFS -  tc: O(n), sc: O(d)
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         maxSum = -float('inf')

#         def maxPathSumRecur(node):
#             if not node:
#                 return 0
            
#             leftSubtreeSum = maxPathSumRecur(node.left) 
#             rightSubtreeSum = maxPathSumRecur(node.right)

#             nonlocal maxSum
#             maxSum = max(maxSum, node.val, node.val + leftSubtreeSum, node.val + rightSubtreeSum, node.val + leftSubtreeSum + rightSubtreeSum)

#             return max(node.val, node.val+leftSubtreeSum, node.val+rightSubtreeSum)
        
#         maxPathSumRecur(root)

#         return maxSum