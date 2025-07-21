from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        
        maxOr = 0
        for num in nums:
            maxOr |= num

        memo = {}
        
        def dfs(index, currOr):
            if index==n:
                return int(currOr==maxOr)
            
            key = (index,currOr)
            if key in memo:
                return memo[key]

            memo[key] = dfs(index+1, currOr) + dfs(index+1, currOr|nums[index])
            return memo[key]

        return dfs(0,0)                


# Input: nums = [3,2,1,5]
# Output: 6

# 1 = [1,3,5]
# 10 = [2,3]
# 100 = [5]

# 