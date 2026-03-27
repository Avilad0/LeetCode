from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([ str(len(s)) + '#' + s for s in strs])

    def decode(self, s: str) -> List[str]:
        decodedList = []

        n = len(s)
        i=0
        while i<n:
            currLen = 0
            while s[i]!='#':
                currLen = currLen*10 + int(s[i])
                i+=1
            
            decodedList.append( s[i+1: i+1+currLen])

            i+=1+currLen
            print(i)
        
        return decodedList
