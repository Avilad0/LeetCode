from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        zeroToNum = [i for i in range(n)]
        numToN = [i for i in range(n-1,-1,-1)]

        ans = []
        minn = n-1

        for [u,v] in queries:
            if zeroToNum[v] > zeroToNum[u]+1:
                zeroToNum[v] = zeroToNum[u]+1
            if numToN[u]> numToN[v]+1:
                numToN[u] = numToN[v]+1

            if zeroToNum[v]+numToN[v]<minn:
                minn=zeroToNum[v]+numToN[v]
            ans.append(minn)

        return ans
    

# print(Solution().shortestDistanceAfterQueries(n = 5, queries = [[2,4],[0,2],[0,4]])) # [3,2,1]
# print(Solution().shortestDistanceAfterQueries(n = 4, queries = [[0,3],[0,2]])) # [1,1]
print(Solution().shortestDistanceAfterQueries(n = 7, queries = [[4,6],[0,3]])) # [5,3]

'''
'''