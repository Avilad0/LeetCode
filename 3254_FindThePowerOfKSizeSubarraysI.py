from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n==1 or k==1:
            return nums

        ans = [-1]*(n-k+1)
        counter = 1

        for i in range(n-1):
            if nums[i]+1==nums[i+1]:
                counter+=1
            else:
                counter=1
            
            if counter>=k:
                ans[i-k+2] = nums[i+1]
        return ans

# class Solution:
#     def resultsArray(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         if n==1 or k==1:
#             return nums

#         ans = [-1]*(n-k+1)
#         i,j=0,1

#         while i <= (n-k):
#             while j < (i+k) and nums[j] == nums[j-1]+1:
#                 j+=1
            
#             if j==i+k:
#                 ans[i]=nums[j-1]
#                 i+=1
#             else:
#                 i=j
#                 j+=1

#         return ans
    

# print(Solution().resultsArray(nums = [1,2,3,4,3,2,5], k = 3)) #Output: [3,4,-1,-1,-1]
# print(Solution().resultsArray(nums = [2,2,2,2,2], k = 4)) #Output: [-1,-1]
# print(Solution().resultsArray(nums = [3,2,3,2,3,2], k = 2)) #Output: [-1,3,-1,3,-1]
print(Solution().resultsArray(nums = [1,3,4], k = 2)) #Output: [3,4]