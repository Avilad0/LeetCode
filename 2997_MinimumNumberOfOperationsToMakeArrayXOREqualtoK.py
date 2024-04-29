from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor =0
        for n in nums:
            xor = xor ^ n

        # faster than 96.5% but higher memory than below
        return bin(xor ^ k).count('1')

        # faster than 74%, lower memory usage than above
        # t = xor ^ k
        # ans = 0
        # while t:
        #     ans += t&1
        #     t>>=1
        # return ans


        # slower than above but still above 50%
        # i=0
        # while xor != k:
        #     if (k & (1<<i)) != (xor & (1<<i)):
        #         ans+=1
        #         xor ^= (1<<i)
        #     i+=1

        # return ans


print(Solution().minOperations(nums = [2,1,3,4], k = 1))
print(Solution().minOperations(nums = [2,0,2,0], k = 0))

# 100
# 100 & 1 == (1 & 1)