class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = 0
        upper = 0
        for c in word:
            i = ord(c)
            if i>96:
                lower = lower | (0b1<<(i-97))
            else:
                upper = upper | (0b1<<(i-65))

        i = 0
        common = lower & upper
        ans =0
        while common:
            t= common & 0b1
            if t:
               ans+=1
            common>>=0b1
            i+=1

        return ans