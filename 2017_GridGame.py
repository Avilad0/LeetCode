from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        sum0 = sum(grid[0]) - grid[0][0]
        sum1 = 0
        
        min_score = sum0
        for i in range(1,n-1):
            sum0 -= grid[0][i]
            sum1 += grid[1][i-1]
            min_score = min(min_score, max(sum0, sum1))

        return min(min_score, sum1+grid[1][n-2])   

print(Solution().gridGame(grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]))  #63

'''
answer: 63
grid = [[20, 3,20,17, 2,12,15,17, 4,15],
        [20,10,13,14,15, 5, 2, 3,14, 3]]

prefix:  20, 23, 43, 60, 62, 74, 89,106,110,125
         99, 79, 69, 56, 42, 27, 22, 20, 17,  3
        
'''

# same as above but with more memory O(n)
# class Solution:
#     def gridGame(self, grid: List[List[int]]) -> int:
#         n = len(grid[0])
#         prefix_sum = [[0]*n for _ in range(2)]
#         prefix_sum[0][0] = grid[0][0]
#         prefix_sum[1][n-1] = grid[1][n-1]
#         for i in range(1,n):
#             prefix_sum[0][i] = prefix_sum[0][i-1] + grid[0][i]
#             prefix_sum[1][n-1-i] = prefix_sum[1][n-i] + grid[1][n-1-i]
        
#         min_score = prefix_sum[0][n-1]-prefix_sum[0][0]
#         for i in range(1,n-1):
#             min_score = min(min_score, max(prefix_sum[0][n-1]-prefix_sum[0][i], prefix_sum[1][0]-prefix_sum[1][i]))

#         return min(min_score, prefix_sum[1][0]-prefix_sum[1][n-1])