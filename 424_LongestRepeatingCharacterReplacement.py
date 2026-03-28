# n= len(s) , m = len(set(s))

# tc = O(n) , sc = (m)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        
        maxLen = 0
        freq = {}
        maxFreq = 0

        l = 0
        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1

            maxFreq=max(maxFreq, freq[s[r]])

            # we don't reinitialize maxFreq when we move l, 
            # because maxLen can only increase if (r-l+1) increase
            # and since k is constant, maxFreq should also increase to keep the window valid
            # and new increased maxFreq will be initialized later if more freq in windows is found.
            
            while r-l+1 - maxFreq > k:
                freq[s[l]]-=1
                l+=1
            
            maxLen = max(maxLen, r-l+1)

        return maxLen
    


# # tc = O(m*n) , sc = (m)
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
        
#         n = len(s)
        
#         maxLen = 0
#         uniqueChars = set(s)

#         for ch in uniqueChars:
#             l = 0
#             count = 0
#             for r in range(n):
#                 if ch == s[r]:
#                     count+=1

#                 while r-l+1 - count > k:
#                     if s[l]==ch:
#                         count-=1
#                     l+=1
                
#                 maxLen = max(maxLen, r-l+1)
        
#         return maxLen