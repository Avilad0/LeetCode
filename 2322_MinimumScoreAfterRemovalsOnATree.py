from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)

        adjList = [[] for _ in range(n)]
        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        
        totalXor = 0
        for num in nums:
            totalXor^=num
        
        ans = float('inf')

        def dfs2(node, parent, xorFirstTree, rootFirstTree):
            xorSecondTree = nums[node]

            for next in adjList[node]:
                if next!=parent:
                    xorSecondTree^=dfs2(next, node, xorFirstTree, rootFirstTree)
            
            if parent != rootFirstTree:            
                nonlocal ans
                xorThirdTree = totalXor^xorFirstTree^xorSecondTree
                ans = min(ans, max(xorFirstTree, xorSecondTree, xorThirdTree) - min(xorFirstTree, xorSecondTree, xorThirdTree) )

            return xorSecondTree


        def dfs1(node, parent):
            xorFirstTree = nums[node]

            for next in adjList[node]:
                if next!=parent:
                    xorFirstTree^=dfs1(next, node)
            
            if parent!=-1:
                dfs2(parent, node, xorFirstTree, node)
            
            return xorFirstTree

        dfs1(0, -1)
        return ans