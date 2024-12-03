from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        i=0
        for j in spaces:
            result.append(s[i:j])
            i=j

        result.append(s[i:])
        return " ".join(result)

# class Solution:
#     def addSpaces(self, s: str, spaces: List[int]) -> str:
#         result = []
#         i,j=0,0
#         n,m =len(s), len(spaces)
#         for _ in range(n+m):
#             if j<m and spaces[j]==i:
#                 result.append(" ")
#                 j+=1
#             else:
#                 result.append(s[i])
#                 i+=1

#         return "".join(result)