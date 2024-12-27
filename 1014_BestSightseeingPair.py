from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_left = values[0]
        max_score = 0

        for i in range(1,n):
            current_right = values[i]-i
            max_score = max(max_score, max_left + current_right)

            current_left = values[i]+i
            max_left = max(current_left, max_left)
            
        return max_score
        

'''
Input: values = [8,1,5,2,6]
Output: 11
8+5-(2-0) = 11

Input: values = [8,1,1,6,7]
Output: 12
8+6-(3-0) = 11
8+7-(4-0) = 11
6+7-(4-3) = 12

'''