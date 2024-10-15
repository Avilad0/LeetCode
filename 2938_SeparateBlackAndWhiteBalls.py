# both solution equally good
# class Solution:
#     def minimumSteps(self, s: str) -> int:
#         n = len(s)
#         positionSum = 0
#         onesCount =0
#         for i in range(n):
#             if s[i]=='1':
#                 positionSum+=i
#                 onesCount+=1

#         return ((n*(n-1))//2) - (((n-1-onesCount)*(n-onesCount))//2) - positionSum



class Solution:
    def minimumSteps(self, s: str) -> int:
        totalSwaps = 0
        onesCount =0
        for c in s:
            if c=='1':
                onesCount+=1
            else:
                totalSwaps += onesCount

        return totalSwaps