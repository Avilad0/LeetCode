from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isComplete = False

class Solution:

    max =0
    def buildTrie(self, arr):
        root = TrieNode()
        for num in arr:
            node = root
            for digit in str(num):
                if digit not in node.children:
                    node.children[digit] = TrieNode()
                node = node.children[digit]
            node.isComplete = True
        return root

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        root1 = self.buildTrie(arr1)
        root2 = self.buildTrie(arr2)

        self.dfs(root1,root2,0)

        return self.max
    
    def dfs(self, node1: TrieNode, node2: TrieNode, depth: int):
        
        if self.max<depth:
            self.max = depth
        
        for child1 in node1.children:
            if child1 in node2.children:
                self.dfs(node1.children[child1], node2.children[child1], depth+1)


print(Solution().longestCommonPrefix(arr1 = [1,10,100], arr2 =[1000])) #3