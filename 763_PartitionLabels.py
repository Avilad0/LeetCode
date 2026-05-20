from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        
        lastIndex = {}
        for i in range(n):
            lastIndex[s[i]]=i
        
        ans = []
        currLen = 0
        maxCurrIndex = 0

        for i in range(n):
            maxCurrIndex = max(maxCurrIndex, lastIndex[s[i]])
            currLen+=1
            if i==maxCurrIndex:
                ans.append(currLen)
                currLen=0
        
        return ans
