class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        onceNum = 0
        for num in nums:
            onceNum^=num
        
        return onceNum