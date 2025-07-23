class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x>=y:
            chr1, chr2 = 'a', 'b'
        else:
            x,y = y,x
            chr1, chr2 = 'b', 'a'

        score = 0
        
        def calc(newS, c1, c2, plusScore):
            stck = ['']
            nonlocal score
            for c in newS:
                if c==c2 and stck[-1]==c1:
                    stck.pop()
                    score += plusScore
                else:
                    stck.append(c)
            
            return "".join(stck)
        

        newS = calc(s, chr1, chr2, x)
        calc(newS, chr2, chr1, y)

        return score