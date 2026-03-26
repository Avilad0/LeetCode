class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        n=len(s)
        charFreq = [0]*26
        for i in range(n):
            charFreq[ord(s[i])-97] +=1
            charFreq[ord(t[i])-97] -=1

        for f in charFreq:
            if f!=0:
                return False
        return True


# class Solution:
#     # def isAnagram(self, s: str, t: str) -> bool:
#     #     if len(s) != len(t):
#     #         return False
#     #     return ''.join(sorted(list(s))) == ''.join(sorted(list(t)))
        

#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
        