from typing import List, Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        r = []
        l = len(nums)
        for i in range(l):
            n = abs(nums[i])
            if nums[n-1]<0:
                r.append(n)
            else:
                nums[n-1]*=-1
        return r

        #slower but less memory
        # b=0b0
        # r = []
        # for n in nums:
        #     b = b ^ (0b1<<n)
        #     if (b>>n) & 1 == 0:
        #         r.append(n)
        
        # return r
    
        #faster but more memory
        # freq = Counter(nums)
        # r=[]
        # for n , f in freq.items():
        #     if f == 2:
        #         r.append(n)
        # return r


print(Solution().findDuplicates([1,2,3,1,3]))