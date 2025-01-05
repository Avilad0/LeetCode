from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        dp = [0]*(n+1)
        for start, end, direction in shifts:
            dp[start]+= (1 if direction else -1)
            dp[end+1]+= (-1 if direction else 1)

        for i in range(1,n):
            dp[i]+=dp[i-1]

        list_of_chars = []
        for i in range(n):
            list_of_chars.append( chr( (ord(s[i]) - 97 + dp[i])%26 + 97) )              

        return "".join(list_of_chars)

# TLE
# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
#         list_of_chars = list(s)
#         for start, end, direction in shifts:
#             for i in range(start,end+1):
#                 list_of_chars[i] = chr( (ord(list_of_chars[i]) - 97 + (1 if direction else -1))%26 + 97)
        
#         return "".join(list_of_chars)
    

print(Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])) #Output: "ace"

'''
s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"

i   shift1  shift2  shift3
0:  -1      -1      0
1:  -1       0      1        
2:   0       1      1
'''