from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf') 
        maxProft = 0

        for price in prices:
            maxProft = max(maxProft, price-minPrice)
            minPrice = min(minPrice, price)

        return maxProft