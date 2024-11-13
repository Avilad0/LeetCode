from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                result += right - left
                left += 1
            else:
                right -= 1
        return result


print(Solution().countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))

'''
nums = [0,1,7,4,4,5], lower = 3, upper = 6 , ans = 6

0,1,7,4,4,5

'''



# #TLE
# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         count = 0
#         n = len(nums)

#         for i in range(n):
#             for j in range(i+1, n):
#                 if lower<=nums[i]+nums[j]<=upper:
#                     count+=1
        
#         return count
