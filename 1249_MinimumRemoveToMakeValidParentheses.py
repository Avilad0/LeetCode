class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count =0
        ans =""
        for c in s:
            if c!="(" and c!=")":
                ans+=c
                continue
            
            if c==')' and count>0:
                count-=1
                ans+=c
                continue
            
            if c=='(':
                count+=1
                ans+=c
            
        i=len(ans)-1
        while count!=0 and i>=0:
            if ans[i]=="(":
                count-=1
                ans= ans[:i] + ans[i+1:]
            i-=1


        return ans
                
print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
print(Solution().minRemoveToMakeValid("a)b(c)d"))
print(Solution().minRemoveToMakeValid("))(("))