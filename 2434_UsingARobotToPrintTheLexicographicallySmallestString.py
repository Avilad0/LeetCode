from collections import defaultdict

class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        maxIndexes = defaultdict(int)
        for i in range(n):
           maxIndexes[s[i]] = i                

        stck = []
        ans = []
        currIndex = 0
        for c in sorted(maxIndexes.keys()):

            while stck and stck[-1]<=c:
                ans.append(stck[-1])
                stck.pop()
            
            if maxIndexes[c]<currIndex:
                continue

            for i in range(currIndex, maxIndexes[c]+1):
                if s[i]==c:
                    ans.append(c)
                else:
                    stck.append(s[i])
            
            currIndex = maxIndexes[c]+1

        stck.reverse()
        ans.extend(stck)

        return "".join(ans)