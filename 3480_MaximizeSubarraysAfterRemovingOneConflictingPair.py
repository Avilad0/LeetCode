from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        lastConflicting = [n+1]*(n+1)
        secondLastConflicting = [n+1]*(n+1)

        for n1,n2 in conflictingPairs:
            if n1>n2:
                n1,n2 = n2, n1
            
            if lastConflicting[n1]>n2:
                secondLastConflicting[n1] = lastConflicting[n1]
                lastConflicting[n1] = n2
            else:
                secondLastConflicting[n1] = min(secondLastConflicting[n1], n2)
        
        
        ans = 0
        firstElementConflictingToExclude, secondElementToExclude = n, n+1
        additionalSubsWithDeletedConPairs = [0]*(n+1)
        for start in range(n,0, -1):
            if lastConflicting[firstElementConflictingToExclude] > lastConflicting[start]:
                secondElementToExclude = min(secondElementToExclude, lastConflicting[firstElementConflictingToExclude], secondLastConflicting[start])
                firstElementConflictingToExclude = start
            else :
                secondElementToExclude = min(secondElementToExclude, lastConflicting[start])

            ans += lastConflicting[firstElementConflictingToExclude] - start
            additionalSubsWithDeletedConPairs[firstElementConflictingToExclude] += secondElementToExclude - lastConflicting[firstElementConflictingToExclude]
        
        return ans + max(additionalSubsWithDeletedConPairs)


print(Solution().maxSubarrays(n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]))   #12
print(Solution().maxSubarrays( n = 4, conflictingPairs = [[2,3],[1,4]]))   #9





'''
Input: n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]
Output: 12

12345
with all con..pairs =   1   234     34  45  5       =   1+ 3 + 2 + 2 + 1   = 9
with 1st removed =      1234    234    34  45  5    =   4 + 3 + 2 + 2 + 1  = 12
with 2nd removed =      1   234     34  45  5       =   1  + 3 + 2 + 2 + 1 = 9
with 3rd removed =      1   234 345 45  5           =   1  + 3 + 3 + 2 + 1 = 10



Input: n = 4, conflictingPairs = [[2,3],[1,4]]
Output: 9

1234
with all con..pairs =   12   2 34  4        =   2 + 1 + 2 + 1 = 6
with 1st removed =      123   234  34  4    =   3 + 3 + 2 + 1 = 9
with 2nd removed =      12   2  34  4       =   2 + 1 + 2 + 1 = 6
'''