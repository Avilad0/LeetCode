from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()
        for num in nums:
            if num in seenNums:
                return True
            
            seenNums.add(num)
 
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) < len(nums)