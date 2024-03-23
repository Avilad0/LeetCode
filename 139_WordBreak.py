from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        l = len(s)+1
        dp = [False]*l
        dp[0] = True
        wordDictSet = set(wordDict)
        
        for j in range(1, l):
            for i in range(0,j):
                if dp[i] and s[i:j] in wordDictSet:
                    dp[j] = True
                    break

        return dp[l-1]


        # dp = [[-1 for _ in __] for __ in wordDict]
        # index = [0 for _ in wordDict]

        # l = len(wordDict)
        # for c in range(len(s)):
        #     for j in range(l):
        #         if c==wordDict[index[j]]:
        #             dp[j][index[j]] = 1
        #             index[j]+=1