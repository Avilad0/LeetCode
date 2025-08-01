from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalsTriangle = [[1]]
        
        for row in range(2,numRows+1):
            nextRow = [1]
            for i in range(row-2):
                nextRow.append(pascalsTriangle[-1][i] + pascalsTriangle[-1][i+1])
            nextRow.append(1)
        
            pascalsTriangle.append(nextRow)
        

        return pascalsTriangle