from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count= 0

        for num in nums:
            mul, isEven = 10, False
            while num//mul!=0:
                isEven = not isEven
                mul*=10
            
            if isEven:
                count+=1

        return count