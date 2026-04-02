from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currProduct = 1
        firstNegativeProduct = None
        maxP = nums[0]

        for num in nums:
            currProduct *= num
            maxP = max(maxP, currProduct)
            if firstNegativeProduct:
                maxP = max(maxP, currProduct//firstNegativeProduct)

            if num == 0:
                currProduct=1
                firstNegativeProduct = None
            elif num<0 and not firstNegativeProduct:
                firstNegativeProduct = currProduct            

        return maxP