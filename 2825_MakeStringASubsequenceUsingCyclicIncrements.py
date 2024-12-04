class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        if len(str2)>n:
            return False
        
        i = 0
        for c in str2:
            while i<n and c!=str1[i] and c!=chr(((ord(str1[i])-96)%26) + 97):
                i+=1
            if i==n:
                return False
            i+=1
        
        return True


# print(Solution().canMakeSubsequence(str1 = "abc", str2 = "ad")) #True
print(Solution().canMakeSubsequence(str1 = "om", str2 = "nm")) #False
