# # same complexity but using map and no remove operation. Only O(n).
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        maxLen = 0

        indexes = {}
        prev = 0
        for i in range(n):
            if s[i] in indexes:
                prev = max(prev,indexes[s[i]]+1)

            maxLen = max(maxLen, i-prev+1)
            indexes[s[i]]=i

        return maxLen


# # same complexity but using set and more remove operation. causes O(2n).
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         n = len(s)
#         maxLen = 0

#         charsSeen = set()
#         l = 0
#         for r in range(n):
#             while s[r] in charsSeen:
#                 charsSeen.remove(s[l])
#                 l+=1
                
#             charsSeen.add(s[r])
#             maxLen = max(maxLen, r-l+1)

#         return maxLen