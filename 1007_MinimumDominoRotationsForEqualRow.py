from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n= len(tops)

        def flipsRequired(num):
            topFlips, bottomFlips = 0, 0
            for i in range(n):
                if tops[i]!=num and bottoms[i]!=num:
                    return -1
                
                if tops[i]!=num:
                    topFlips+=1
                if bottoms[i]!=num:
                    bottomFlips+=1
            
            return min(topFlips, bottomFlips)

        flips1 = flipsRequired(tops[0])
        flips2 = flipsRequired(bottoms[0])

        if flips1==-1 and flips2==-1:
            return -1
        elif flips1==-1:
            return flips2
        elif flips2==-1:
            return flips1
        
        return min(flips1, flips2)



# class Solution:
#     def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
#         n, freq = len(tops), [0]*7
#         for i in range(n):
#             freq[tops[i]]+=1
#             if tops[i]!=bottoms[i]:
#                 freq[bottoms[i]]+=1
        
#         maxFreq = 0
#         for i in range(1,7):
#             if maxFreq==-1 or freq[maxFreq]<freq[i]:
#                 maxFreq=i
        
#         if freq[maxFreq]<n:
#             return -1
        
#         topRotations = 0
#         bottomRotations = 0
#         for i in range(n):
#             if tops[i]!=maxFreq:
#                 topRotations+=1
#             if bottoms[i]!=maxFreq:
#                 bottomRotations+=1
        
#         return min(topRotations, bottomRotations)