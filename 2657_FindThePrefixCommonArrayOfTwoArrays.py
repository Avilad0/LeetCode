from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        set_removed = set()
        ans = [0]*n
        for i in range(n-1, -1, -1):
            ans[i] = n - len(set_removed)
            set_removed.add(A[i])
            set_removed.add(B[i])
        
        return ans
    
# can also be done using bitmasking