from typing import List
from bisect import bisect_right

# By finding largest number for the current number (more than it) such that target is achieved and counting all subsequence between them
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0

        nums.sort()
        n = len(nums)

        powerOf2 = [1]
        for _ in range(n):
            powerOf2.append((powerOf2[-1]*2)%MOD)

        for left in range(n):
            if nums[left]*2>target:
                break

            maxPairAllowed = target-nums[left]
            right = bisect_right(nums, maxPairAllowed, left+1)-1

            ans = (ans + powerOf2[right-left])%MOD

        return ans


# # With caching Sum of Powers of 2
# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         MOD = 10**9 + 7
#         ans = 0

#         nums.sort()
#         n = len(nums)

#         sumOfPowersOf2 = [1]
#         for _ in range(n):
#             sumOfPowersOf2.append((sumOfPowersOf2[-1]*2)%MOD)

#         for right in range(n):
#             maxPairAllowed = target-nums[right]
#             left = bisect_right(nums, maxPairAllowed,0, right+1)

#             toAdd = sumOfPowersOf2[right]
#             toSubtract = 0 if right<left else sumOfPowersOf2[right-left]

#             ans = (ans + toAdd - toSubtract)%MOD

#         return ans


# # TLE as not caching sum of powers of 2
# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         MOD = 10**9 + 7
#         ans = 0

#         nums.sort()
#         n = len(nums)

#         for right in range(n):
#             maxPairAllowed = target-nums[right]
#             left = bisect_right(nums, maxPairAllowed,0, right+1)

#             # if left>right:
#             #     ans +=1
#             # else:
#             for i in range(left):
#                 if right-i-1<=0:
#                     ans+=1
#                 else:
#                     ans = (ans + (1<<(right-i-1)))%MOD

#         return ans

print(Solution().numSubseq(nums = [3,5,6,7], target = 9)) #4 
print(Solution().numSubseq(nums = [3,3,6,8], target = 10)) #6 


'''
sumOfPowerOf2 = 1 2 4 8 16 32 64
indexes       = 0 1 2 3  4  5  6


if right =5, left =4 , eligible = 0,1,2,3

(2**4 + 2**3 + 2**2 + 2**1 + 2**0 + 2**0) - (2**0 + 2**0)
sumOfPowerOf2[right] - sumOfPowerOf2[right-left] = 32 - 2 = 30

'''

'''
indexes       = 0 1 2 3  4  5  6

if left =1, right = 4, 
must include  = 1, optional = 2,3,4

1 * 2 * 2 * 2 = 2**(3) = 2**(right-left)

'''