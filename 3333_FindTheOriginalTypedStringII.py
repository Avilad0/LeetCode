# Optimized DP with prefix Sum solution
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)

        MOD = 10**9 + 7
        charCounts = []
        count = 1
        for i in range(1,n):
            if word[i-1]!=word[i]:
                charCounts.append(count)
                count = 1
            else:
                count+=1
        
        charCounts.append(count)
        charCountsN = len(charCounts)

        totalPossibilities = 1
        for f in charCounts:
            totalPossibilities = (totalPossibilities*f)%MOD

        if charCountsN>=k:
            return totalPossibilities
        
        dp = [0]*k  #dp[i][j] = no. of str of length j using i diff chars
        dp[0] = 1

        for currCount in charCounts:
            prefixSum = [dp[0]]
            for i in range(1,k):
                prefixSum.append(prefixSum[i-1] + dp[i])

            dp = [0]*k
            for dpJ in range(1, k):                
                dp[dpJ] = (prefixSum[dpJ-1] - ( 0 if dpJ-1-currCount<0 else prefixSum[dpJ-1-currCount]) + MOD)%MOD

        lessThanK = sum(dp)
        return (totalPossibilities - lessThanK + MOD)%MOD
    


# # DP with prefix Sum solution
# class Solution:
#     def possibleStringCount(self, word: str, k: int) -> int:
#         n = len(word)

#         MOD = 10**9 + 7
#         charCounts = []
#         count = 1
#         for i in range(1,n):
#             if word[i-1]!=word[i]:
#                 charCounts.append(count)
#                 count = 1
#             else:
#                 count+=1
        
#         charCounts.append(count)
#         charCountsN = len(charCounts)

#         totalPossibilities = 1
#         for f in charCounts:
#             totalPossibilities = (totalPossibilities*f)%MOD

#         if charCountsN>=k:
#             return totalPossibilities
        
#         dp = [[0]*k for _ in range(charCountsN+1)]  #dp[i][j] = no. of str of length j using i diff chars
#         dp[0][0] = 1

#         prefixSum = [[0]*k for _ in range(charCountsN+1)]
#         prefixSum[0] = [1]*k

#         for i in range(charCountsN):
#             dpI = i+1
#             for dpJ in range(1, k):                
#                 dp[dpI][dpJ] = (prefixSum[dpI-1][dpJ-1] - ( 0 if dpJ-1-charCounts[i]<0 else prefixSum[dpI-1][dpJ-1-charCounts[i]]) + MOD)%MOD
#                 prefixSum[dpI][dpJ] = (prefixSum[dpI][dpJ-1] + dp[dpI][dpJ]) %MOD

#         lessThanK = prefixSum[charCountsN][k-1]
#         return (totalPossibilities - lessThanK + MOD)%MOD



# # TLE for very large strings
# class Solution:
#     def possibleStringCount(self, word: str, k: int) -> int:
#         n = len(word)

#         if n<k:
#             return 0
#         if n==k:
#             return 1
        
#         MOD = 10**9 + 7
#         charCounts = []
#         count = 1
#         for i in range(1,n):
#             if word[i-1]!=word[i]:
#                 charCounts.append(count)
#                 count = 1
#             else:
#                 count+=1
        
#         charCounts.append(count)
#         charCountsN = len(charCounts)

#         totalPossibilities = 1
#         for f in charCounts:
#             totalPossibilities = (totalPossibilities*f)%MOD

#         if charCountsN>k:
#             return totalPossibilities
        
#         memo = {}
#         def dfs(index, remaining) -> int:
#             if index == charCountsN:
#                 if remaining >= 0:
#                     return 1    
#                 return 0 
            
#             key = (index, remaining)
#             if key in memo:
#                 return memo[key]
            
#             if index == charCountsN-1:
#                 count = min(remaining , charCounts[index])
#             else :            
#                 count = 0
#                 for toUse in range(1, charCounts[index]+1):
#                     if remaining-toUse< (charCountsN - index-1):
#                         break
#                     else:
#                         count = (count + dfs(index+1, remaining-toUse))%MOD
            
#             memo[key] = count
#             return count

#         return (totalPossibilities - dfs(0, k-1))%MOD
 


# print(Solution().possibleStringCount(word = "aaabbb", k = 3))
# print(Solution().possibleStringCount(word = "aabbccdd", k = 7))
# print(Solution().possibleStringCount(word = "aabbccdd", k = 8))

print(Solution().possibleStringCount(word = "bbbbxxn" ,k = 6)) # Output = 3



'''
Input: word = "aaabbb", k = 3
Output: 8

aaabbb
aaabb
aaab
aab
aabb
aabbb
abbb
abb
'''