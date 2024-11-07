from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxFreq = 0
        for i in range(24):
            currMax = 0
            andBit = 1<<i
            for num in candidates:
                if num & andBit:
                    currMax+=1

            if currMax>maxFreq:
                maxFreq=currMax
                
        return maxFreq

# class Solution:
#     def largestCombination(self, candidates: List[int]) -> int:
#         freq = {i:0 for i in range(27)}
#         for num in candidates:
#             binary = bin(num)[2:]
#             for i,c in enumerate(binary[::-1]):
#                 freq[i]+= (c=='1')

#         return max(freq.values())

'''
Input: candidates = [16,17,71,62,12,24,14]
Output: 4

16:   10000
17:   10001
71: 1000111
62:  111110
12:    1100
24:   11000
14:    1110

'''


