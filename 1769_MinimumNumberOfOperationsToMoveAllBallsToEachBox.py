from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]
        left_ones, right_ones, n = 0,0, len(boxes)
        for i in range(n-1,0, -1):
            if boxes[i] == '1':
                right_ones+=1    
            ans[0] += right_ones
        
        if boxes[0]=='1':
            left_ones+=1
        for i in range(1,n):
            ans.append( ans[i-1] - right_ones + left_ones)
            if boxes[i]=='1':
                left_ones+=1
                right_ones-=1

        return ans




# 1-pass
# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         n = len(boxes)
#         answer = [0] * n

#         balls_to_left = 0
#         moves_to_left = 0
#         balls_to_right = 0
#         moves_to_right = 0

#         for i in range(n):
#             answer[i] += moves_to_left
#             balls_to_left += int(boxes[i])
#             moves_to_left += balls_to_left

#             j = n - 1 - i
#             answer[j] += moves_to_right
#             balls_to_right += int(boxes[j])
#             moves_to_right += balls_to_right

#         return answer
    
print(Solution().minOperations(boxes = "001011"))  #Output: [11,8,5,4,3,4]
print(Solution().minOperations(boxes = "110"))  #Output: [1,1,3]

        
'''
Input: boxes = "110"
Output: [1,1,3]

for 0th place: 0 1 1 = 1
for 1th place:   

Input: boxes = "001011"
Output: [11,8,5,4,3,4]

0: 11
0: 11 -3 + 0 = 8
1: 8  -3 + 0 = 5
0: 5  -2 + 1 = 4
1: 4  -2 + 1 = 3
1: 3  -1 + 2 = 4

'''