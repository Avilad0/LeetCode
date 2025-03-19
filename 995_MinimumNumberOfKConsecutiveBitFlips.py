from typing import List
from collections import deque

# Time Complexity: O(n) , Space Complexity: O(k)
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        queueFlips = deque()
        n = len(nums)
        ans, unsetBit = 0, 0
        
        for i in range(n):

            if i >= k:
                unsetBit ^= queueFlips.popleft()

            if nums[i] == unsetBit:
                if i>n-k:
                    return -1
                ans += 1
                unsetBit ^= 1
                queueFlips.append(True)
            else :
                queueFlips.append(False)
        
        return ans

# # Time Complexity: O(n) , Space Complexity: O(n)
# class Solution:
#     def minKBitFlips(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         bitFlips = [0]* (n+1)
#         ans, currFlips = 0, 0
#         for i in range(n-k+1):
#             currFlips += bitFlips[i]
#             if nums[i] == currFlips%2:
#                 ans += 1
#                 bitFlips[i+1]+=1
#                 bitFlips[i+k]-=1

#         for i in range(n-k+1, n):
#             currFlips += bitFlips[i]
#             if nums[i] == currFlips%2:
#                 return -1
        
#         return ans

# class Solution:
#     def minKBitFlips(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         bitFlips = [0]* (n+1)
#         ans, curr, unsetBit= 0, 0, 0
#         for i in range(n-k+1):
#             curr += bitFlips[i]
#             if (nums[i] == unsetBit and curr%2==0) or (nums[i] != unsetBit and curr%2==1):
#                 ans += 1
#                 bitFlips[i+1]+=1
#                 bitFlips[i+k]-=1

#         for i in range(n-k+1, n):
#             curr += bitFlips[i]
#             if (nums[i] == unsetBit and curr%2==0) or (nums[i] != unsetBit and curr%2==1):
#                 return -1
        
#         return ans


print(Solution().minKBitFlips(nums = [0,0,0,1,0,1,1,0], k = 3))