class Solution:
    def minimumLength(self, s: str) -> int:
        
        n1 = 0
        n2 = len(s)-1
        while n2-n1>=1 and s[n1] == s[n2]:
            while n1<n2 and (s[n1]==s[n1+1] or s[n2] == s[n2-1]):
                if s[n1+1] == s[n1]:
                    n1=n1+1
                if s[n2-1] == s[n2]:
                    n2=n2-1
            
            if n1>=n2:
                return 0
            
            n1= n1+1
            n2= n2-1
                
        return n2-n1+1