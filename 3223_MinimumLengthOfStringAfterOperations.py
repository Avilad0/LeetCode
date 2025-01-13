class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0]*26
        for c in s:
            freq[ord(c)-97]+=1
        
        ans = len(s)
        for i in range(26):
            if freq[i]>2:
                ans = ans - freq[i] + 1 + (freq[i]+1)%2
                # if freq[i]%2:
                #     ans = ans - freq[i] + 1
                # else:
                #     ans = ans - freq[i] + 2
        
        return ans