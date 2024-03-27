from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        s,e = 0,0
        l = len(nums)
        pr=nums[0]
        ans=0
        while e<l:
            flag = False
            if pr<k:
                ans+=1+e-s
                flag = True
            
            if flag or s==e:
                e+=1
                if e==l:
                    break
                pr = pr * nums[e]
            else:
                pr = pr // nums[s]
                s+=1

        return ans
    

#[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
print(Solution().numSubarrayProductLessThanK([10,5,2,6],100))