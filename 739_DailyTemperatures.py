from typing import List

# tc=O(n), sc=O(1) - DP (dp directly used ans array and not additional space)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans = [0]*n

        for i in range(n-2, -1,-1):
            j=i+1
            while j<n and temperatures[j]<=temperatures[i]:
                if ans[j]==0:
                    j=n
                    break

                j+=ans[j]
            
            if j<n:
                ans[i]=j-i

        return ans

# tc=O(n), sc=O(n) - monotonic stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n

        stck = [] #(temp[i],i)
        for i in range(n):
            while stck and stck[-1][0]<temperatures[i]:
                ans[stck[-1][1]] = i-stck[-1][1]
                stck.pop()
            
            stck.append((temperatures[i],i))
        
        return ans
    
