from typing import Counter,List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # solution in space complexity O(1)
        # count, m = 1, nums[0]
        # for i in nums[1:]:
        #     if count ==0:
        #         m = i
        #     if i == m:
        #         count+=1
        #     else:
        #         count-=1
        
        # return m

        for i,freq in Counter(nums).items():
            if freq*2 > len(nums):
                return i
            
print(Solution().majorityElement([1,2,2,1,2]))