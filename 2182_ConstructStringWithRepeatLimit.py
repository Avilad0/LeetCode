class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        freq = [0]*26
        for c in s:
            freq[ord(c)-97]+=1

        ans = []
        for i in range(25,-1,-1):
            k=i-1
            for j in range(freq[i]):
                if j>0 and j%repeatLimit == 0:
                    while k>=0 and freq[k]<1:
                        k-=1
                    if k==-1:
                        return ''.join(ans)
                    freq[k]-=1
                    ans.append(chr(k+97))
                ans.append(chr(i+97))
        
        return ''.join(ans)

#TLE  
# class Solution:
#     def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
#         s = list(s)
#         s.sort(reverse=True)
#         n, prev, count = len(s),'',0
#         for i in range(n):
#             if prev == s[i]:
#                 if count>=repeatLimit:
#                     j=i+1
#                     while j<n and s[j]==s[i]:
#                         j+=1
#                     if j==n:
#                         return "".join(s[:i])
#                     s[i],s[j] = s[j],s[i]
#                     prev , count = s[i], 1
#                 else:
#                     count+=1
#             else:
#                 prev, count = s[i], 1
        
#         return "".join(s)

