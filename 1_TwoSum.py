from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in map:
                return [i, map[dif]]
            map[nums[i]] = i