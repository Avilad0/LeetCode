class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     return ''.join(sorted(list(s))) == ''.join(sorted(list(t)))
        

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        