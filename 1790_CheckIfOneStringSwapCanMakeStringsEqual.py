class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap1, swap2 = None,None

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if swap1==None:
                    swap1=s1[i]
                    swap2=s2[i]
                elif swap1=='':
                    return False
                else:
                    if s2[i]!=swap1 or s1[i]!=swap2:
                        return False
                    else:
                        swap1,swap2 = '', ''
        
        return swap1==None or swap1==''