from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans =0
        num_set=set()
        for n in nums:
            if n in num_set:
                ans^=n
            else:
                num_set.add(n)

        return ans