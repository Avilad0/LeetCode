from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        n2 = n*n

        sumOfNums = sum(x for row in grid for x in row)
        sumOfNumSquares = sum(x*x for row in grid for x in row)

        correctSumOfNums = (n2*(n2+1))//2
        correctSumOfNumSquares = (n2*(n2+1)*(2*n2+1))//6

        missingMinusRepeating = correctSumOfNums - sumOfNums
        missingPlusRepeating = (correctSumOfNumSquares - sumOfNumSquares)//missingMinusRepeating

        return [ (missingPlusRepeating-missingMinusRepeating)//2, (missingPlusRepeating+missingMinusRepeating)//2 ]
        



'''
    n(n+1)/2 = sum -repeated +missing
    missing-repeated = n(n+1)/2 - sum

    n(n+1)(2n+1)/6 = sumOfSquares - repeated^2 + missing^2
    missing^2 -repeated^2 = n(n+1)(2n+1)/6 - sumOfSquares
    (missing-repeated)(missing+repeated) = n(n+1)(2n+1)/6 - sumOfSquares


'''