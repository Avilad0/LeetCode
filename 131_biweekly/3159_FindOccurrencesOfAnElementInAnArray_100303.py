from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ans =[]
        i = []
        for j in range(len(nums)):
            if x==nums[j]:
                i.append(j)
        
        l = len(i)
        for q in queries:
            if q>l:
                ans.append(-1)
            else:
                ans.append(i[q-1])

        return ans
    

print(Solution().occurrencesOfElement(nums = [1,3,1,7], queries = [1,3,2,4], x = 1))  #Output: [0,-1,2,-1]