class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            left = right = i
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
                ans+=1
                        
            left, right = i, i+1
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
                ans+=1

        
        return ans