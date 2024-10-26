from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_depths = {}
        subtree_heights = {}

        first_largest_height = {}
        second_largest_height = {}

        def _dfs(node, level):
            if not node:
                return 0

            node_depths[node.val] = level

            left_height = _dfs(node.left, level + 1)
            right_height = _dfs(node.right, level + 1)
            current_height = 1 + max(left_height, right_height)

            subtree_heights[node.val] = current_height

            if current_height > first_largest_height.get(level, 0):
                second_largest_height[level] = first_largest_height.get(level, 0)
                first_largest_height[level] = current_height
            elif current_height > second_largest_height.get(level, 0):
                second_largest_height[level] = current_height

            return current_height

        _dfs(root, 0)

        return [
            node_depths[q]
            + (
                second_largest_height.get(node_depths[q], 0)
                if subtree_heights[q] == first_largest_height[node_depths[q]]
                else first_largest_height.get(node_depths[q], 0)
            )
            - 1
            for q in queries
        ]


# class Solution:
#     depthAndAlternateHeight = {}
#     def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
#         height = self.dfs1(root, 0)
#         self.dfs2(root)


    
#     def dfs1(self, node: Optional[TreeNode], depth: int) -> int:
#         leftHeight = 0
#         rightHeight = 0
#         if node.left:
#             leftHeight = self.dfs1(node.left, depth+1)
#             self.depthAndAlternateHeight[node.left.val] = [depth+1, leftHeight]
#         if node.right:
#             rightHeight = self.dfs1(node.right, depth+1)
#             self.depthAndAlternateHeight[node.right.val] = [depth+1, rightHeight]

#         return max(leftHeight,rightHeight)+1
    
#     def dfs2(self, node: Optional[TreeNode]):

#         alternateHeight = self.depthAndAlternateHeight[node.val][1]
#         if node.left and node.right:
#             self.node.left

# '''
# alternateHeightOfNode = max(heightOfsibling,alternateHeightofParent)
# '''