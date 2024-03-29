from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)

        l =len(nums)
        indexes =[-1]
        for i in range(l):
            if nums[i]==m:
                indexes.append(i)

        l_i =len(indexes)
        if l_i<1+k:
            return 0
        
        ans = 0
        for i in range(1,l_i-k+1):
            ans = ans + ((indexes[i]-indexes[i-1]) * (l-indexes[i+k-1]))

        return ans


print(Solution().countSubarrays([1,3,2,3,3],2))

print(Solution().countSubarrays([1,3,2,1,2],2))

# [1,3,2,3,3], k = 2
# -1 [1,3,4] 5

# 2*2 + 2*1 = 6