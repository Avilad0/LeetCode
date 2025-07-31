from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        currORs = {0}

        for curr in arr:
            currORs = {curr|ors for ors in currORs} | {curr}
            ans.update(currORs)

        return len(ans)