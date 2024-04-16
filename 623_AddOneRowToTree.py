from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth==1:
            return TreeNode(val,root)

        def checkAndAddNode(node, d):

            if node == None:
                return
            
            if d==0:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val,None, node.right)
                return
            
            
            checkAndAddNode(node.left, d-1)
            checkAndAddNode(node.right, d-1)
        
        checkAndAddNode(root,depth-2)
        return root
    
print(Solution().addOneRow(TreeNode(4,TreeNode(2,TreeNode(3),TreeNode(1)),TreeNode(6,TreeNode(5))),1,2))

#[4,2,6,3,1,5] , 1, 2
#             4
#     2               6
# 3       1       5

# output:
#             4
#         1       1
#     2               6
#   3   1           5