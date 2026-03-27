from typing import List

# O(nm)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs)==1:
            return [strs]
        
        n=len(strs)

        charFreqs = {}
        for i in range(n):
            f=[0]*26
            for c in strs[i]:
                f[ord(c)-97]+=1
            fTuple = tuple(f)
            if fTuple in charFreqs:
                charFreqs[fTuple].append(strs[i])
            else:
                charFreqs[fTuple] = [strs[i]]
        
        return list(charFreqs.values())
        

# # O(nm + n^2)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         if len(strs) == 1:
#             return [strs]

#         n = len(strs)
#         charFreqs = [[0]*26 for _ in range(n)]

#         for i in range(n):
#             for c in strs[i]:
#                 charFreqs[i][ord(c)-97]+=1

#         processed = set()
#         ans = []
#         for i in range(n):
#             if i in processed:
#                 continue
            
#             currGrp = [strs[i]]
#             processed.add(i)
#             for j in range(i+1,n):
#                 if j in processed:
#                     continue
                
#                 valid = True
#                 for k in range(26):
#                     if charFreqs[i][k]!=charFreqs[j][k]:
#                         valid=False
                
#                 if valid:
#                     currGrp.append(strs[j])
#                     processed.add(j)
                
#             ans.append(currGrp)

#         return ans


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         if strs.__len__()==1:
#             return [strs]
        
#         rMap = {}

#         for s in strs:
#             p = ''.join(sorted(list(s)))
#             if rMap.__contains__(p):
#                 rMap[p].append(s)
#             else:
#                 rMap[p] = [s]


#         return list(rMap.values())