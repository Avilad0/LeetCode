from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        left, right, ans = -1, 0 , []
        for i in range(n):
            if nums[i]==key:
                left = max(right,i-k)
                right = min(n, i+k+1)
                for j in range(left, right):
                    ans.append(j)
        return ans


# class Solution:
#     def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
#         n = len(nums)
#         frontPrefix, reversePrefix, ans = -1, -1, set()
#         for i in range(n):
#             if nums[i]==key:
#                 frontPrefix=k
#             if frontPrefix>=0:
#                 ans.add(i)

#             frontPrefix-=1
        
#             if nums[n-1-i]==key:
#                 reversePrefix=k
#             if reversePrefix>=0:
#                 ans.add(n-1-i)

#             reversePrefix-=1
        
                
#         ans = list(ans)
#         ans.sort()
#         return ans