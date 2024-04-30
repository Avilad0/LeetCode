class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [0]*1024
        cnt[0]=1
        ans = 0
        mask = 0
        for c in word:
            idx = ord(c) -97
            mask^= 1<<idx
            ans+=cnt[mask]
            for i in range(10):
                look = mask^(1<<i)
                ans += cnt[look]
            cnt[mask]+=1
        
        return ans
    
print(Solution().wonderfulSubstrings("aba"))
print(Solution().wonderfulSubstrings("aabb"))
print(Solution().wonderfulSubstrings("he"))