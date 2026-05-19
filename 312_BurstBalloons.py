class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]

        memo = {}
        def dfs(left, right):
            if right<left:
                return 0
            
            if (left, right) not in memo:
                maxVal = 0
                for mid in range(left, right+1):
                    currVal = nums[left-1]*nums[mid]*nums[right+1]
                    currVal += dfs(left,mid-1)+dfs(mid+1, right)
                    maxVal = max(maxVal, currVal)
                memo[(left,right)]=maxVal
            return memo[(left, right)]

        return dfs(1,len(nums)-2)