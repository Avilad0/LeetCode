from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque([root])
        while queue:
            arr = []
            for i in range(len(queue)):
                node = queue.popleft()
                arr.append((node.val, i))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans += self.getSwaps(arr)
        return ans
    
    def getSwaps(self, arr: List[int]) -> int:
        indexMap = { arr[i]:i for i in range(len(arr)) }
        sortedArr = sorted(arr)
        swaps = 0
        for i in range(len(arr)):
            if arr[i]!= sortedArr[i]:
                swaps+=1
                swapPos = indexMap[sortedArr[i]]
                arr[i], arr[swapPos] = arr[swapPos], arr[i]
                indexMap[arr[i]], indexMap[arr[swapPos]] = i, swapPos

        return swaps