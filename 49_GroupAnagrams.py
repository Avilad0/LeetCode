from typing import List


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         if strs.__len__()==1:
#             return [strs]
        
#         rMap = {}

#         for s in strs:
#             p = 0b0
#             for c in s:
#                 p = p | (0b1 <<(ord(c) -97)) 

#             if rMap.__contains__(str(p)):
#                 rMap[str(p)].append(s)
#             else:
#                 rMap[str(p)] = [s]
        

#         return [sorted(i) for i in list(rMap.values())]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs.__len__()==1:
            return [strs]
        
        rMap = {}

        for s in strs:
            p = ''.join(sorted(list(s)))
            if rMap.__contains__(p):
                rMap[p].append(s)
            else:
                rMap[p] = [s]


        return list(rMap.values())