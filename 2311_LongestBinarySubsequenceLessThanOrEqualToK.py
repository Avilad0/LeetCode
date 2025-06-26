class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n, ans = len(s),0
        curr= 0
        kBits = k.bit_length()
        
        for i in range(n-1,-1,-1):
            if s[i]=='1':
                pos = n-1-i
                if pos<kBits and curr+(1<<pos)<=k:
                    ans+=1
                    curr += (1<<pos)
            elif s[i]=='0':
                ans+=1

        return ans
    

# class Solution:
#     def longestSubsequence(self, s: str, k: int) -> int:
#         n, ans = len(s),0
#         curr, multiplier = 0, 1
        
#         for i in range(n-1,-1,-1):
#             if s[i]=='1':
#                 if curr+multiplier<=k:
#                     ans+=1
#                     curr += multiplier
#             elif s[i]=='0':
#                 ans+=1

#             multiplier*=2
                
#         return ans
    
print(Solution().longestSubsequence(s = "1001010", k = 5))
print(Solution().longestSubsequence("001010101011010100010101101010010", 93951055)) #31