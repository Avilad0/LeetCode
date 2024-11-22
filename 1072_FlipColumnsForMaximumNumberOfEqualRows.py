from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        patternFreq = {}

        for row in matrix:
            row = "".join( '0' if cell==row[0] else '1' for cell in row )
            patternFreq[row] = patternFreq.get(row,0)+1


        return max(patternFreq.values())

'''
[[0,0,0],[0,0,1],[1,1,0]]
000
001
110

==

000
001
001

000 : 1
001 : 2

ans =2

'''