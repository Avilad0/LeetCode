from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        ans = 0
        count = 0
        min_positive = float('inf')
        max_negative = float('-inf')

        for n in nums:
            ans+=n
            xorValue = n^k

            change=xorValue-n

            if change>0:
                ans+=change
                count^=1
                if change<min_positive:
                    min_positive = change
            else:
                if change>max_negative:
                    max_negative = change

        if count==0:
            return ans

        return max(ans-min_positive, ans+max_negative) 


print(Solution().maximumValueSum(nums = [78,43,92,97,95,94], k = 6, edges = [[1,2],[3,0],[4,0],[0,1],[1,5]])) #507
print(Solution().maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]])) #6
print(Solution().maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]])) #9
print(Solution().maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]])) #42