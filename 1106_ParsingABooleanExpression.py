class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operatorsStack = []
        operandsStack = [[]]

        for c in expression:
            if c == 't':
                operandsStack[-1].append(True)
            elif c == 'f':
                operandsStack[-1].append(False)
            elif c == ',':
                continue
            elif c == '(':
                operandsStack.append([])
            elif c == ')':
                if operatorsStack[-1]== '!':
                    operandsStack[-2].append(not operandsStack[-1][0])
                elif operatorsStack[-1]=='&':
                    operandsStack[-2].append(not (False in operandsStack[-1]))
                else:
                    operandsStack[-2].append(True in operandsStack[-1])
                
                operandsStack.pop()
                operatorsStack.pop()                    

            else:
                operatorsStack.append(c)

        return operandsStack[0][0]


# print(Solution().parseBoolExpr("&(|(f))"))
# print(Solution().parseBoolExpr("!(&(f,t))"))

print(Solution().parseBoolExpr("|(&(t,f,t),!(t))"))


'''
"|(&(t,f,t),!(t))"

stack1 = [|,&]
stack2 = [[],[],[t,f,t],]

stack1 = [|]
stack2 = [[],[f]]

stack1 = [|,!]
stack2 = [[],[f],[t]]

stack1 = [|]
stack2 = [[],[f,f]]

stack1 = []
stack2 = [[f]]

'''




# class Solution:
#     def parseBoolExpr(self, expression: str) -> bool:
#         stack = []
#         isOpenBracket = False

#         for c in expression:
#             if c == '(':
#                 isOpenBracket = True
#             elif c==')':
#                 isOpenBracket = False
#                 if stack[-2]=='!':
#                     stack[-1] = not stack[-1]
#                 stack.pop(-2)

#             elif c==',':
#                 continue
            
#             elif isOpenBracket and type(stack[-1]) == bool:
#                 if stack[-2]=='&':
#                     if (not stack[-1]) or c=='f':
#                         stack[-1] = False
#                     else:
#                         stack[-1] = True
#                 else:
#                     if stack[-1] or c=='t':
#                         stack[-1] = True
#                     else:
#                         stack[-1] = False

#             elif c =='f':
#                 stack.append(False)
#             elif c== 't':
#                 stack.append(True)
#             else:
#                 stack.append(c)

#         return stack[0]