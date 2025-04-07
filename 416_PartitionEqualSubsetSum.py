from typing import List

# Bottom-Up DP, Tabulation - Using bitmask (maybe only possible in python)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        
        toFind = total//2
        dp = 1

        for num in nums:
            dp = dp | (dp<<num)  # shift all set bits by num and OR the 2 to get all possible sums (set bits)
        
        print(dp)
        return (dp & (1<<toFind)) != 0
    

    

# # Bottom-Up DP, Tabulation - Using set (can be done using list too)
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total%2:
#             return False
        
#         toFind = total//2
#         dp = set([0])

#         for num in nums:
#             for currentSum in list(dp):
#                 if num+currentSum<=toFind:
#                     dp.add(num+currentSum)
                           
#             if toFind in dp:
#                 return True
        
#         return False




# # Bottom-Up DP, Tabulation 
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total%2:
#             return False
        
#         n= len(nums)
#         toFind = total//2
#         dp = [False]*(toFind+1)
#         dp[0]=True

#         for i in range(n):
#             for j in range(toFind, nums[i]-1, -1):
#                 dp[j] = dp[j] | dp[j-nums[i]]
            
#             if dp[toFind]:
#                 return True
        
#         return False




# # Top-down DP, memoization
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total%2:
#             return False
        
#         n= len(nums)
#         toFind = total//2
#         memo = {}
#         def backtrack(i, currentSum):
            
#             if (currentSum==toFind):
#                 return True

#             if i==n or currentSum>toFind:
#                 return False
            
#             if (i,currentSum) in memo:
#                 return memo[(i, currentSum)]


#             memo[(i, currentSum)] = backtrack(i+1, currentSum+nums[i]) or backtrack(i+1, currentSum)
#             return memo[(i, currentSum)]
        
#         return backtrack(0,0)