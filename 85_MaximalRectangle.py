from typing import List,Deque

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        area = 0
        r= len(matrix[0])
        hist = [0]*r
        for row in matrix:
            for i in range(r):
                hist[i] = hist[i] + 1 if row[i] == '1' else 0
            area = max(area, self.maxArea(hist))
        
        return area
    
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        stack = Deque()
        l= len(heights)
        for i in range(l + 1):
            while stack and (i == l or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                area = max(area, h * w)
            stack.append(i)
        
        return area


    
print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(Solution().maximalRectangle([["0","0","1","1"],["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]))
print(Solution().maximalRectangle([["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]))




# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:

#         r = len(matrix)
#         c = len(matrix[0])

#         horizontal = [[0]*(c+1) for i in range(r)]
#         vertical = [[0]*c for i in range((r+1))]
#         horizontal_count_columns_min = [0]*c
#         horizontal_count_rows_max = [0]*r
#         vertical_count_columns_max = [0]*c
#         vertical_count_rows_min = [0]*r
#         ans= 0

#         for i in range(r):
#             for j in range(c):
#                 if matrix[i][j]=="1":
#                     horizontal[i][j+1]= horizontal[i][j]+1
#                     vertical[i+1][j]= vertical[i][j]+1

#                     horizontal_count_columns_min[j] = horizontal[i][j+1] if horizontal_count_columns_min[j]==0 else min(horizontal[i][j+1], horizontal_count_columns_min[j]) 
#                     horizontal_count_rows_max[i] = max(horizontal_count_rows_max[i], horizontal[i][j+1])
#                     vertical_count_columns_max[j] = max(vertical_count_columns_max[j], vertical[i+1][j])
#                     vertical_count_rows_min[i]= vertical[i+1][j] if vertical_count_rows_min[i]==0 else min(vertical[i+1][j], vertical_count_rows_min[i])

#                     # ans = max(ans, max( min(horizontal[:][j+1])*max(vertical[1:][j]) , max(horizontal[i][1:])*min(vertical[i+1][:])  ) )
#                     ans = max(ans, max( horizontal_count_columns_min[j]*vertical_count_columns_max[j] , horizontal_count_rows_max[i]*vertical_count_rows_min[i]  ) )

#                 else:
#                     horizontal[i][j+1]=0
#                     vertical[i+1][j]=0

#                     horizontal_count_columns_min[j] = 0
#                     horizontal_count_rows_max[i] =0
#                     vertical_count_columns_max[j]=0
#                     vertical_count_rows_min[i]=0


#         print(horizontal)
#         print(vertical)

#         return ans



        # r = len(matrix)
        # c = len(matrix[0])

        # horizontal = []
        # for i in matrix:
        #     temp = [i[0]]
        #     for j in range(1,c):
        #         if i[j]=="1":
        #             temp.append(temp[-1]+1)
        #         else:
        #             temp.append(0)
        #     horizontal.append(temp)
        
        # vertical = []
        # rec = []
        # ans = 0
        # for j in range(c):
        #     temp = matrix[0][j]
        #     temp_a = matrix[0][j]
        #     for i in range(1,r):
        #         if matrix[i][j]=="1":
        #             temp.append(temp[-1]+1)

        #             if ans<:
        #                 ans =
        #         else:
        #             temp.append(0)
        #             temp_a.append(0)
        #     vertical.append(temp[1:])
        
        # ans = []




    #     max_breadth = 0
    #     max_length = 0
    #     ans = 0 
    #     return self.findArea(max_breadth,max_length, ans,0,0)
        
    # def findArea(self, max_breadth,max_length, ans, i, j) -> int:
    #     if ans[i][j]