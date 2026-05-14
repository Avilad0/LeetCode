from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        for token in tokens:
            if token=="+":
                b = stck.pop()
                a = stck.pop()
                stck.append(a+b)
            elif token=="-":
                b = stck.pop()
                a = stck.pop()
                stck.append(a-b)
            elif token=="*":
                b = stck.pop()
                a = stck.pop()
                stck.append(a*b)
            elif token=="/":
                b = stck.pop()
                a = stck.pop()
                stck.append(int(a/b))
            else:
                stck.append(int(token))
        
        return stck[0]