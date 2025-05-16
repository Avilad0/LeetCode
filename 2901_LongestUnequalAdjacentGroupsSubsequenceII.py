from functools import cache
from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def areConditionsSatisfied(i, j):
            if groups[i]==groups[j] or  len(words[i])!=len(words[j]):
                return False

            diffs = 0
            for k in range(len(words[i])):
                if words[i][k]!=words[j][k]:
                    if diffs>0:
                        return False
                    diffs+=1

            return True

        n=len(words)
        dp = [1]*n
        prev = [-1]*n

        for i in range(1,n):
            for j in range(i):
                if areConditionsSatisfied(i,j) and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    prev[i] = j
        
        maxEndingIndex, maxLength = 0, dp[0]
        for i in range(1,n):
            if dp[i]>maxLength:
                maxLength = dp[i]
                maxEndingIndex = i
        
        ans = []
        while maxEndingIndex!=-1:
            ans.append(words[maxEndingIndex])
            maxEndingIndex = prev[maxEndingIndex]
        
        ans.reverse()
        return ans


# # Can calculate longest sequence size with this
# class Solution:
#     def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
#         n= len(groups)

#         def areConditionsSatisfied(w1, w2):
#             if len(w1)!=len(w2):
#                 return False
            
#             diffs = 0
#             for i in range(len(w1)):
#                 if w1[i]!=w2[i]:
#                     if diffs>0:
#                         return False
#                     diffs+=1
            
#             return True
        
#         @cache
#         def dfs(prevWordIndex, currWordIndex):
#             if currWordIndex==n:
#                 return 0
                
#             maxLength = dfs(prevWordIndex, currWordIndex+1)
            
#             if prevWordIndex == -1 or (groups[prevWordIndex]!=groups[currWordIndex] and areConditionsSatisfied(words[prevWordIndex], words[currWordIndex])):
#                 withI = 1+dfs(currWordIndex,currWordIndex+1)
#                 if withI>maxLength:
#                     maxLength = withI
            
#             return maxLength
        

#         return dfs(-1, 0)

    
print(Solution().getWordsInLongestSubsequence(["bab","dab","cab"], [1,2,2])) # ["bab","dab"] or ["bab","cab"]