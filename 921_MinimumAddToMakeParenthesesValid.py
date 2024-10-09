class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        opening, changes = 0,0
        for c in s:
            if c==')':
                if opening>0:
                    opening-=1
                else:
                    changes+=1
            else:
                opening+=1

        return opening+changes