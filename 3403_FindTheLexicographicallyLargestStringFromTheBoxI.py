class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word

        n, i, j = len(word), 0, 1

        while j<n:
            k=0
            while j+k<n and word[i+k]==word[j+k]:
                k+=1
            
            if j+k<n and word[i+k]<word[j+k]:
                i,j = j, max(j+1,i+k+1)
            else:
                j=j+k+1
        
        return word[i: min(n, i+ n-numFriends+1)]


# class Solution:
#     def answerString(self, word: str, numFriends: int) -> str:
#         if numFriends==1:
#             return word
        
#         n, i = len(word), 0
#         largestChar = max(word)
#         maxWordLenPossible = n-numFriends+1
#         maxString = ""

#         def updateMaxStringWith(start, end):
#             nonlocal maxString
#             l1,l2 = end-start, len(maxString)

#             for i in range(min(l1,l2)):
#                 if word[start + i]>maxString[i]:
#                     maxString = word[start:end]
#                     return
#                 elif word[start+i]<maxString[i]:
#                     return
            
#             if l1>l2:
#                 maxString = word[start:end]


#         for i in range(n):
#             if word[i]==largestChar:
#                 updateMaxStringWith(i, min(i+maxWordLenPossible, n))

#         return maxString
    
# print(Solution().answerString(word ="nbjnc", numFriends = 2))
print(Solution().answerString(word = "jcooek" , numFriends = 4))