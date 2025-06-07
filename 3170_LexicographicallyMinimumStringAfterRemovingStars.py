class Solution:
    def clearStars(self, s: str) -> str:
        indexes = [[] for _ in range(26)]
        n = len(s)
        ans = list(s)

        for i in range(n):
            if ans[i]=='*':
                for j in range(26):
                    if indexes[j]:
                        ans[indexes[j].pop()] = '*'
                        break
            else:
                indexes[ord(ans[i])-97].append(i)


        return "".join(ans[i] for i in range(n) if ans[i]!='*' )
    

# class Solution:
#     def clearStars(self, s: str) -> str:
#         indexes = {}
#         indexesToRemove = set()
#         minChar = None
#         n = len(s)

#         for i in range(n):
#             if s[i]=='*':
#                 indexesToRemove.add(i)
#                 indexesToRemove.add(indexes[minChar][-1])
#                 if len(indexes[minChar]) == 1:
#                     indexes.pop(minChar)
#                     if not indexes:
#                         minChar = None
#                     else:
#                         while minChar not in indexes:
#                             minChar = chr(ord(minChar) + 1)
#                 else:
#                     indexes[minChar].pop()
#             else:
#                 if s[i] in indexes:
#                     indexes[s[i]].append(i)
#                 else:
#                     indexes[s[i]] = [i]
#                     if not minChar or s[i]<minChar:
#                         minChar = s[i]


#         ans = [s[i] for i in range(n) if i not in indexesToRemove]

#         return "".join(ans)