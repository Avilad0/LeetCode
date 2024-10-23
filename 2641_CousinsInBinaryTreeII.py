from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = [root]
        sums = []
        while queue:
            summ = 0
            temp = []
            for node in queue:
                summ+=node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            sums.append(summ)
            queue = temp

        queue.append(root)
        root.val=0

        while queue:
            temp =[]
            for node in queue:
                
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                    
                queue = temp


        return root