class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        totalNSum = (n*(n+1))//2
        maxMMultiplier = n//m
        divisibleByMSum = m * ( (maxMMultiplier*(maxMMultiplier+1))//2 )

        return (totalNSum - divisibleByMSum) - divisibleByMSum

# class Solution:
#     def differenceOfSums(self, n: int, m: int) -> int:
#         diff = 0
#         for i in range(1,n+1):
#             if i%m==0:
#                 diff -= i
#             else:
#                 diff += i
        
#         return diff