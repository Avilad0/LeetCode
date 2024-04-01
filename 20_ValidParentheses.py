class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {"[":"]", "{":"}", "(":")"}
        dic_set = dic.keys()
        stack = []
        i=-1
        for c in s:
            if c in dic_set:
                stack.append(c)
                i+=1
            elif i==-1 or c!= dic[stack.pop()]:
                return False
            else:
                i-=1

        return i==-1
    

        # stack = []
        # i=-1
        # for c in s:
        #     if c == "]":
        #         if i==-1 or stack[i]!="[":
        #             return False
        #         else:
        #             stack.pop()
        #             i-=1

        #     elif c == "}":
        #         if i==-1 or stack[i]!="{":
        #             return False
        #         else:
        #             stack.pop()
        #             i-=1

        #     elif c == ")":
        #         if i==-1 or stack[i]!="(":
        #             return False
        #         else:
        #             stack.pop()
        #             i-=1
        #     else:
        #         stack.append(c)
        #         i+=1

        # return i==-1

