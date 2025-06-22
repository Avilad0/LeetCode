from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = [s[i-k:i] for i in range(k,n+1,k)]

        if n%k:
            ans.append( s[n-(n%k):] + fill*(k- (n%k)))
            
        return ans