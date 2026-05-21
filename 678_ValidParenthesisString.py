# tc=O(n), sc=O(1) - 2 pointers
class Solution:
    def checkValidString(self, s: str) -> bool:

        openMin, openMax = 0, 0

        for i in range(len(s)):
            if s[i]=="(":
                openMin, openMax = openMin+1, openMax+1
            elif s[i]==")":
                openMin, openMax = openMin-1, openMax-1
            else:
                openMin, openMax = openMin-1, openMax+1
            
            if openMax<0:
                return False
            if openMin<0:
                openMin=0

        return openMin==0
        




# #tc=O(n), sc=O(n) -  2 stacks
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         opening_bracket = []
#         asterisk = []
        
#         for i, c in enumerate(s):
#             if c == '(':
#                 opening_bracket.append(i)
#             elif c == ')':
#                 if opening_bracket:
#                     opening_bracket.pop()
#                 elif asterisk:
#                     asterisk.pop()
#                 else:
#                     return False
#             else:
#                 asterisk.append(i)
        
#         while opening_bracket and asterisk:
#             if opening_bracket[-1] < asterisk[-1]:
#                 opening_bracket.pop()
#                 asterisk.pop()
#             else:
#                 break
        
#         return len(opening_bracket) == 0
    

#False
print(Solution().checkValidString("(")) 
print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
"(((((*(((((*((**((**((((**))*)*)))))))))((*(((((**(**)"

#True
print(Solution().checkValidString("(*)"))
print(Solution().checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))



#((((*())))