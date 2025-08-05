from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        n = len(baskets)

        for fruit in fruits:
            isBasketFound = False
            for i in range(n):
                if baskets[i]>=fruit:
                    baskets[i]=0
                    isBasketFound = True
                    break

            if not isBasketFound:
                unplaced +=1

        return unplaced