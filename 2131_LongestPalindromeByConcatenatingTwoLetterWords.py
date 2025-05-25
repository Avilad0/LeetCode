from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freqOfPalindromes = defaultdict(int)
        maxLen = 0
        doubleWordCount = 0

        for word in words:
            if word[0]==word[1]:
                if freqOfPalindromes[word]>0:
                    maxLen+=2
                    freqOfPalindromes[word]-=1
                    doubleWordCount-=1
                else:
                    freqOfPalindromes[word]=1
                    doubleWordCount+=1

            else:
                rev = word[1]+word[0]
                if freqOfPalindromes[rev]>0:
                    maxLen+=2
                    freqOfPalindromes[rev]-=1
                else:
                    freqOfPalindromes[word]+=1

        if doubleWordCount>0:
            maxLen+=1
        
        return maxLen*2
    

# class Solution:
#     def longestPalindrome(self, words: List[str]) -> int:
#         freqOfPalindromes = defaultdict(int)
#         for word in words:
#             freqOfPalindromes[word] += 1
        

#         isSinglePresent = False
#         maxLen = 0
#         for word,f in freqOfPalindromes.items():
#             if word[0]==word[1]:
#                 if f&1:
#                    isSinglePresent=True
#                    maxLen += f - 1
#                 else:               
#                    maxLen += f
#             elif word[0]<word[1]:
#                 rev = word[1] + word[0]
#                 if rev in freqOfPalindromes:
#                     maxLen += 2*min(f,freqOfPalindromes[rev])
        
#         if isSinglePresent:
#             maxLen+=1
        
#         return maxLen*2