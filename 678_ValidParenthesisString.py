class Solution:
    def checkValidString(self, s: str) -> bool:
        opening_bracket = []
        asterisk = []
        
        for i, c in enumerate(s):
            if c == '(':
                opening_bracket.append(i)
            elif c == ')':
                if opening_bracket:
                    opening_bracket.pop()
                elif asterisk:
                    asterisk.pop()
                else:
                    return False
            else:
                asterisk.append(i)
        
        while opening_bracket and asterisk:
            if opening_bracket[-1] < asterisk[-1]:
                opening_bracket.pop()
                asterisk.pop()
            else:
                break
        
        return len(opening_bracket) == 0
    

#False
print(Solution().checkValidString("(")) 
print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
"(((((*(((((*((**((**((((**))*)*)))))))))((*(((((**(**)"

#True
print(Solution().checkValidString("(*)"))
print(Solution().checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))



#((((*())))