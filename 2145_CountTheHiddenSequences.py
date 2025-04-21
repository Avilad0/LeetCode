from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)+1
        
        currHidden, minHidden, maxHidden = 0, 0, 0
        for i in range(0,n-1):
            currHidden=currHidden+differences[i]
            
            if maxHidden<currHidden:
                maxHidden = currHidden
            if minHidden>currHidden:
                minHidden = currHidden

        if upper-lower < maxHidden-minHidden:
            return 0
        
        return (upper-lower) - (maxHidden-minHidden) + 1
    



# class Solution:
#     def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
#         n = len(differences)+1
        
#         hidden = [0]*n
#         minHidden, maxHidden = 0, 0
#         for i in range(0,n-1):
#             hidden[i+1]=hidden[i]+differences[i]
#             minHidden = min(hidden[i+1], minHidden)
#             maxHidden = max(hidden[i+1], maxHidden)

#         if upper-lower < maxHidden-minHidden:
#             return 0
        
#         return (upper-lower) - (maxHidden-minHidden) + 1