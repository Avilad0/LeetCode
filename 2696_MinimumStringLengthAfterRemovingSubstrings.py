class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if stack and (( s[i]=='B' and stack[-1]=='A') or (s[i]=='D' and stack[-1]=='C')):
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack)


# class Solution:
#     def minLength(self, s: str) -> int:
#         n= len(s)-1
#         i=0
#         sett = set(["AB", "CD"])

#         while i<n:
#             if s[i]+s[i+1] in sett:
#                 s= s[:i] + s[i+2:]
#                 n-=2
#                 if i>0:
#                     i-=1
#             else:
#                 i+=1
        
#         return n+1