from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniques = set()
        n = len(nums)

        for i in range(n-1, -1,-1):
            if nums[i] not in uniques:
                uniques.add(nums[i])
            else:
                return (i+1)//3 + (0 if (i+1)%3==0 else 1)
        
        return 0