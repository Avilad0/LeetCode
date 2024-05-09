from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        ans = 0
        i=0
        while i<k and happiness[i]-i>0:
            ans+=happiness[i]-i
            i+=1

        return ans
    

print(Solution().maximumHappinessSum(happiness = [1,2,3], k = 2))   #4
print(Solution().maximumHappinessSum(happiness = [1,1,1,1], k = 2)) #1
print(Solution().maximumHappinessSum(happiness = [2,3,4,5], k = 1)) #5
