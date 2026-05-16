from typing import List

# DFS
# tc=O(n*(2^n)), sc = O(n) [for ouput = 2^n subsets and n*(2^(n-1)) integers in output]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        stack = []
        def dfs(i):
            if i==n:
                ans.append(stack[:])
                return
                
            dfs(i+1)

            stack.append(nums[i])
            dfs(i+1)
            stack.pop()

        dfs(0)
        return ans


# Iterative
# tc=O(n*(2^n)), sc = O(1) [for ouput = 2^n subsets and n*(2^(n-1)) integers in output]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            ans += [ subset + [num] for subset in ans]

        return ans