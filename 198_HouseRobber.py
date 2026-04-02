from typing import List

# same as prev but more clear
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevPrevHouse, prevHouse = 0, 0

        for num in nums:
            prevPrevHouse, prevHouse=prevHouse, max(prevHouse, num+prevPrevHouse)

        return prevHouse

# class Solution:
#     def rob(self, inputArr: List[int]) -> int:
#             n=len(inputArr)
#             dp = [0]*(3)
            
#             for i in range(n):
#                 dp[(i+1)%3] = max(dp[(i-1)%3] + inputArr[i], dp[i%3])
                
#             return dp[n%3]