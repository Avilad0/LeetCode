from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minn, negativecount, summ = 100002,0,0

        for row in matrix:
            for num in row:
                if num<0:
                    negativecount+=1
                    num*=-1
                if minn > num:
                    minn=num
                summ+=num
        
        if negativecount%2==0:
            return summ
        else:
            return summ - minn - minn