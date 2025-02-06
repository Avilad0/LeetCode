from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n<4:
            return 0
        
        ans = 0
        map_products = {}
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]*nums[j] in map_products:
                    ans += map_products[nums[i]*nums[j]]
                    map_products[nums[i]*nums[j]] += 8
                else:
                    map_products[nums[i]*nums[j]] = 8

        return ans
    
print(Solution().tupleSameProduct(nums = [2,3,4,6])) #8