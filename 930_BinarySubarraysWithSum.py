from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        s,count,result =0,0,0
                
        for e in range(len(nums)):
            if nums[e]==1:
                goal-=1
                count=0
            
            while goal==0 and s<=e:
                goal+=nums[s]
                s+=1
                count+=1
            
            while goal<0:
                goal+=nums[s]
                s+=1
            
            result+=count

        return result

        
        # TLE for large array
        # l = len(nums)        
        # count = 0
        # for i in range(l):
        #     t = 0
        #     g1 = 0
        #     for j in range(i,l):
        #         g1 = t + nums[j]
        #         if goal == g1:
        #             count+=1
        #         t = g1
        # return count
    

print(Solution().numSubarraysWithSum([1,0,1,0,1],2))