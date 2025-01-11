class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n<k:
            return False
        if n==k:
            return True
        
        odds = 0
        for c in s:
            odds ^= (1<<(ord(c)-97))
        return  bin(odds).count("1")<=k
    

# class Solution:
#     def canConstruct(self, s: str, k: int) -> bool:
#         n = len(s)
#         if n<k:
#             return False
#         if n==k:
#             return True
        
#         odds = [0]*26
#         for c in s:
#             odds[ord(c)-97] ^= 1
#         return sum(odds)<=k
    

# print(Solution().canConstruct(s = "leetcode", k = 3)) #False
# print(Solution().canConstruct(s = "true", k = 4)) #True
print(Solution().canConstruct(s = "qlkzenwmmnpkopu", k = 15)) #True