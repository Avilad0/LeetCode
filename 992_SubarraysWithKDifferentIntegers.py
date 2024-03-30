from typing import List

class Solution:

    def countSubArraysWithMaxKDistinct(self, nums: List[int], k: int) -> int:
        l = len(nums)
        i,j,ans=0,0,0
        freq ={}

        while j<l:
            if nums[j] in freq:
                freq[nums[j]]+=1
            else:
                freq[nums[j]]=1
            
            while i<=j and len(freq)>k:
                freq[nums[i]]-=1
                if freq[nums[i]]==0:
                    freq.pop(nums[i])
                i+=1

            ans=ans + j-i+1
            j+=1

        return ans
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return  self.countSubArraysWithMaxKDistinct(nums,k) - self.countSubArraysWithMaxKDistinct(nums, k-1)



#         freq = {}
#         ans = 0 
        
#         i=0
#         j=0
#         while j<= len(nums)-k and i < len(nums):
#             if k==0 and nums[i] not in freq:   
#                 i-=1            
#                 freq[nums[j]]-=1
#                 if freq[nums[j]]==0:
#                     freq.pop(nums[j])
#                     k+=1
#                 j+=1
#             elif nums[i] in freq:
#                 freq[nums[i]]+=1
#             else:
#                 freq[nums[i]]=1
#                 k-=1

#             if k==0:
#                 ans+=1
            
#             i+=1

#         return ans


print(Solution().subarraysWithKDistinct([1,2,1,3,4],3))
print(Solution().subarraysWithKDistinct([1,2,1,2,3],2))

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
#   1*1 + 1*1 + 1*1
#       
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
#   1*3 + 1*2 + 1*1 + 1*1