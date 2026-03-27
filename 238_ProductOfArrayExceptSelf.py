from typing import List

# tc:O(n)       sc:O(1)
# with using division operation
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        totalProduct = 1
        zeroIndex = -1
        for i in range(n):
            if nums[i]==0:
                if zeroIndex!=-1:
                    return [0]*n
                zeroIndex=i
            else:
                totalProduct*=nums[i]

        if zeroIndex!=-1:
            ans = [0]*n
            ans[zeroIndex] = totalProduct
            return ans

        ans = []
        for num in nums:
            ans.append(totalProduct//num)
        
        return ans
    
# # tc:O(n)       sc:O(1)
# # without using division operation
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         n = len(nums)
#         ans = []
#         currProduct = 1
#         for num in nums:
#             ans.append(currProduct)
#             currProduct*=num

#         suffProduct=nums[-1]
#         for i in range(n-2,-1,-1):
#             ans[i]=ans[i]*suffProduct
#             suffProduct*=nums[i]
        
#         return ans