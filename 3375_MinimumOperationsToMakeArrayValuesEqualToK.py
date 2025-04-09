from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        uniques = set()
        for num in nums:
            if num<k:
                return -1
            
            uniques.add(num)

        if k in uniques:
            uniques.remove(k)
    
        return len(uniques)