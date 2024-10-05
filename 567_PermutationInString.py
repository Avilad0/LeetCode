class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1N = len(s1)
        s2N = len(s2)

        if s2N<s1N:
            return False
        
        s1Freq = [0]*26
        s2Freq = [0]*26
        for i in range(len(s1)):
            s1Freq[ord(s1[i])-97]+=1
            s2Freq[ord(s2[i])-97]+=1

        matchingChars = 0
        for i in range(26):
            if s1Freq[i]==s2Freq[i]:
                matchingChars+=1

        for i in range(0, s2N - s1N):
            if matchingChars == 26:
                return True
            
            charToRemove = ord(s2[i])-97
            charToAdd = ord(s2[i+ s1N])-97


            s2Freq[charToRemove]-=1
            if s2Freq[charToRemove] == s1Freq[charToRemove]:
                matchingChars+=1
            elif s2Freq[charToRemove]+1 == s1Freq[charToRemove]:
                matchingChars-=1

            s2Freq[charToAdd]+=1
            if s2Freq[charToAdd] == s1Freq[charToAdd]:
                matchingChars+=1
            elif s2Freq[charToAdd]-1 == s1Freq[charToAdd]:
                matchingChars-=1
            
        return matchingChars==26


'''
a b c
a b c d e

'''


'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = []

        s2N = len(s2)
        i=0
        while i<s2N:
            tempSet = set(s1)
            j=i
            while j<s2N and (s2[j] in tempSet):
                tempSet.remove(s2[j])
                j+=1
            
            if not tempSet:
                return True
            
            if i==j:
                i+=1
            else:
                i=j
        
        return False
'''