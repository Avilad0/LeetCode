class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        curr = word[0]
        count = 0
        for c in word:
            if curr!=c or count>=9:
                comp.append(str(count))
                comp.append(curr)
                curr = c
                count = 1
            else:
                count+=1
        
        comp.append(str(count))
        comp.append(curr)
        return ''.join(comp)