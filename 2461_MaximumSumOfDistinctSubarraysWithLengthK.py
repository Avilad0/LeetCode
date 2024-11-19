from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i,j,n,maxx,running= 0,0,len(nums),0,0
        seen = set()
        while j<n:
            if nums[j] in seen:
                while i<j and nums[i]!=nums[j]:
                    running-=nums[i]
                    seen.remove(nums[i])
                    i+=1
                i+=1
            else:
                running+=nums[j]
                seen.add(nums[j])
                if j-i+1==k:
                    if running>maxx:
                        maxx=running
                    running-=nums[i]
                    seen.remove(nums[i])
                    i+=1
            
            j+=1
        
        return maxx
    

print(Solution().maximumSubarraySum(nums = [1,1,1,7,8,9], k = 3)) #24