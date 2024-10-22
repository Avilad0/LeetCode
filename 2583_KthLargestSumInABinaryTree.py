from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = {}    
        queue = [(root,0)]
        while queue:
            node,level = queue.pop(0)
            if level in sums:
                sums[level]+=node.val
            else:
                sums[level]=node.val

            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right, level+1))
        if len(sums)<k:
            return -1
        sortedSum = sorted(sums.values(), reverse=True)
        return sortedSum[k-1]