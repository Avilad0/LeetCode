class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i1, i2, n = 0,0, len(start)

        while True:
            while i1<n and start[i1]=='_':
                i1+=1

            while i2<n and target[i2]=='_':
                i2+=1

            if i1==n or i2==n:
                return i1==i2
            
            if start[i1]!=target[i2] or (start[i1]=='R' and i1>i2) or (start[i1]=='L' and i1<i2):
                return False
            
            i1+=1
            i2+=1
        return False

# class Solution:
#     def canChange(self, start: str, target: str) -> bool:
#         c1, c2 = '',''
#         ln1, ln2 = [],[]
#         for i in range(len(start)):
#             if c1==start[i]:
#                 ln1[-1]+=1
#             elif '_'!=start[i]:
#                 ln1.append(1)
#                 c1 =  start[i]
            
#             if c2==target[i]:
#                 ln2[-1]+=1
#             elif '_'!=target[i]:
#                 ln2.append(1)
#                 c2 =  target[i]
        
#         if len(ln1)!=len(ln2):
#             return False
#         for i in range(len(ln1)):
#             if ln1[i]!=ln2[i]:
#                 return False
            
#         return True
    

print(Solution().canChange(start = "_L__R__R_", target = "L______RR"))