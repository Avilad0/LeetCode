from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        ps = [0]*(n+1)

        for query in queries:
            ps[query[0]] += 1
            ps[query[1]+1] -= 1

        for i in range(n):
            if ps[i]<nums[i]:
                return False

            ps[i+1] += ps[i]

        return True