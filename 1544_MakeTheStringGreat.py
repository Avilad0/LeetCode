class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack and stack[-1].lower()==c.lower() and c!=stack[-1]:
                stack.pop()
                continue
            stack.append(c)

        return ''.join(stack)

        # if len(s)==1:
        #     return s
        
        # i=0
        # l=len(s)
        # while i<l-1:
        #     if s[i].lower() == s[i+1].lower() and s[i]!=s[i+1]:
        #         s = s[:i] + s[i+2:]
        #         l = len(s)
        #         i = max(0,i-1)
        #     else:
        #         i+=1

        # return s
    


print(Solution().makeGood("leEeetcode"))
print(Solution().makeGood("abBAcC"))
