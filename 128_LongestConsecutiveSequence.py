from typing import List

# tc: O(n)  sc: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if num-1 not in numsSet:
                currLen = 1
                while num+currLen in numsSet:
                    currLen+=1
                longest = max(currLen, longest)
        
        return longest


# # same complexity, diff way.
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         n=len(nums)
#         if n==0 or n==1:
#             return n

#         parentOnly = set()
#         parentToChildMap = {}

#         for num in nums:
#             if num in parentToChildMap:
#                 continue
            
#             parentToChildMap[num] = None

#             if num-1 in parentToChildMap:
#                 parentToChildMap[num-1] = num
#             else:
#                 parentOnly.add(num)

#             if num+1 in parentToChildMap:
#                 parentToChildMap[num] = num+1
#                 if num+1 in parentOnly:
#                     parentOnly.remove(num+1)
            
#         longest = 1
#         for parent in parentOnly:
#             currNode, currLen = parent, 0
#             while currNode!=None:
#                 currLen+=1
#                 currNode=parentToChildMap[currNode]

#             longest = max(longest, currLen)

#         return longest