from typing import List

# tc=O(n), sc=O(1), floyd algo for entry point of cycle detection
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        while True:
            slow=nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        
        start=0
        while True:
            slow=nums[slow]
            start=nums[start]
            if start==slow:
                return slow
            

# tc=O(32n)=O(n), sc=O(1), bit manipulation (find each bit position expected vs actual counts in arr)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for bit in range(32):
            mask = 1<<bit
            numsBitCount, expectedBitCount = 0, 0
            for i in range(n):
                if nums[i]&mask:
                    numsBitCount+=1
                if i&mask:
                    expectedBitCount+=1
                
            if expectedBitCount<numsBitCount:
                ans|=mask

        return ans                

# # tc=O(n), sc=O(1), manipulating input arr (not recommended)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in range(n):
#             absVal = abs(nums[i])
#             if nums[absVal]<0:
#                 return absVal
#             else:
#                 nums[absVal]*=-1
        
#         return -1