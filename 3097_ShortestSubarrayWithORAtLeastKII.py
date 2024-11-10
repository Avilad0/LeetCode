from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        minn = float('inf')
        left,right = 0,0
        bitCount = [0]*32
        n = len(nums)

        while right<n:
            currOR = self.__updateBitCounts(bitCount, nums[right], 1)

            while left <= right and currOR >= k:
                minn = min(minn, right - left + 1)
                currOR = self.__updateBitCounts(bitCount, nums[left], -1)
                left += 1

            right += 1

        return -1 if minn == float("inf") else minn


    def __updateBitCounts(self, bitCount: list, number: int, delta: int) -> None:
        result = 0
        for pos in range(32):
            if number & (1 << pos):
                bitCount[pos] += delta
    
            if bitCount[pos]:
                result |= (1<<pos)
        
        return result

print(Solution().minimumSubarrayLength(nums = [1,2,32,21], k = 55))

'''
Input: nums = [2,1,8], k = 10
Output: 3

Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

'''