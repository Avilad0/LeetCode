import bisect

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        descI = n-1
        while descI>0 and nums[descI]<=nums[descI-1]:
            descI-=1
        
        if descI==0:
            nums.reverse()
            return 
        
        i = bisect.bisect_left(nums, -nums[descI-1], lo=descI, hi=n, key=lambda x: -x)-1
        nums[descI-1], nums[i] = nums[i], nums[descI-1]

        left, right = descI, n-1
        while left<right:
            nums[left], nums[right]=nums[right], nums[left]
            left, right = left+1, right-1