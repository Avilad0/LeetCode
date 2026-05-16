from typing import List

#tc=O(n*(2^n)), sc=O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        candidates.sort()

        ans = []
        stack = []
        def dfs(i, currSum):
            if currSum==target:
                ans.append(stack[:])
                return

            if i==n or currSum>target:
                return

            for j in range(i, n):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if currSum+ candidates[j]>target:
                    break
                stack.append(candidates[j])
                dfs(j+1, currSum + candidates[j])
                stack.pop()

        dfs(0, 0)
        return ans
