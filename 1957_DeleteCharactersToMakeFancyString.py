class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy = []
        last = ''
        count = 0
        for c in s:
            if c==last:
                if count<2:
                    count+=1
                    fancy.append(c)
            else:
                fancy.append(c)
                last=c
                count=1

        return ''.join(fancy)