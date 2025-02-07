from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        freqOfColors = {}
        labelToColor = {}
        ans = []
        for q in queries:
            if q[0] in labelToColor:
                freqOfColors[labelToColor[q[0]]]-=1
                if freqOfColors[labelToColor[q[0]]] == 0:
                    del freqOfColors[labelToColor[q[0]]]
            

            labelToColor[q[0]]=q[1]
            if q[1] in freqOfColors:
                freqOfColors[q[1]]+=1
            else:
                freqOfColors[q[1]]=1

            ans.append(len(freqOfColors))

        return ans