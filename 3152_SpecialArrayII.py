from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        prefix = [0]
        for i in range(1,len(nums)):
            if nums[i]%2==nums[i-1]%2:
                prefix.append(prefix[i-1]+1)
            else:
                prefix.append(prefix[i-1])
        
        ans = []
        for q in queries:
            ans.append(prefix[q[0]]==prefix[q[1]])

        return ans

# TLE could be improved with binary search
# class Solution:
#     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

#         indexes = []
#         start, prev = 0, nums[0]%2
#         for i in range(1,len(nums)):
#             if nums[i]%2==prev:
#                 indexes.append([start,i-1])
#                 start = i
#             else:
#                 prev = nums[i]%2
#         indexes.append([start,len(nums)])
        
#         iN = len(indexes)
#         ans = []
#         for q in queries:
#             i=0
#             while i<iN and q[0]>=indexes[i][0]:
#                 i+=1
#             i-=1

#             ans.append(q[1] <= indexes[i][1])
#         return ans
    
print(Solution().isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))     #Output: [false,true]