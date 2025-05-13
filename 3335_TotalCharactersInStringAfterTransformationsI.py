from functools import cache

class Solution:
    MOD = 10**9 + 7

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0]*26
        for c in s:
            freq[ord(c)-97]+=1
        
        finalLength = 0
        for i in range(26):
            finalLength = (finalLength + freq[i]*self.countLengthFromZ(t-25+i)) %self.MOD
        
        return finalLength
    
    @cache
    def countLengthFromZ(self, time):
        if time<=0:
            return 1
        
        return (self.countLengthFromZ(time-26) + self.countLengthFromZ(time-25))%self.MOD