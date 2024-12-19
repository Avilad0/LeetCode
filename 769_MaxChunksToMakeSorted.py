from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n= len(arr)
        maxDP = arr[:]
        minDP = arr[:]
        for i in range(1,n):
            maxDP[i]= max(maxDP[i-1], arr[i])
            minDP[n-i-1] = min(minDP[n-i], arr[n-i-1])
        
        count = 1
        for i in range(1, n):
            if maxDP[i-1] < minDP[i]:
                count+=1
        
        return count



print(Solution().maxChunksToSorted(arr = [1,0,2,3,4]))   # Output: 4
print(Solution().maxChunksToSorted([1,2,3,4,5,0]))   # Output: 1    