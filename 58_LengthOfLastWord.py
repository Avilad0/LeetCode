class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # ans =0
        # flag= False
        # for c in s:
        #     if c==" ":
        #         flag=True
        #     else:
        #         if flag:
        #             ans=0
        #             flag=False
        #         ans+=1
        # return ans


        ans=0
        s = s.strip()
        l = len(s)-1
        while s[l]!=" " and l>=0:
            ans+=1
            l-=1
        return ans

        
        # return len(s.split()[-1])
    
print(Solution().lengthOfLastWord(" abcde aa   "))
    

