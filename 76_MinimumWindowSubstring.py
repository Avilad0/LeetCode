#same but storing the indices instead of creating new strings
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tFreq = {}
        for c in t:
            tFreq[c] = tFreq.get(c,0)+1
        
        n=len(s)
        tChN = len(tFreq)

        minSubStr = None
        left, right = 0,0
        winFreq = {}
        matchingChr = 0

        while right<n:
            while right<n and matchingChr!=tChN:
                winFreq[s[right]] = winFreq.get(s[right],0)+1
                if s[right] in tFreq and winFreq[s[right]]==tFreq[s[right]]:
                    matchingChr+=1
                right +=1

            while matchingChr==tChN and left<right:
                winFreq[s[left]] -=1
                if s[left] in tFreq and winFreq[s[left]]==tFreq[s[left]]-1:
                    matchingChr-=1
                    if not minSubStr or minSubStr[1]-minSubStr[0]> right-left:
                        minSubStr = [left, right]

                left +=1

        return s[minSubStr[0]:minSubStr[1]] if minSubStr else ""



#
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
        
#         tFreq = {}
#         for c in t:
#             tFreq[c] = tFreq.get(c,0)+1
        
#         n=len(s)
#         tChN = len(tFreq)

#         minSubStr = None
#         left, right = 0,0
#         winFreq = {}
#         matchingChr = 0

#         while right<n:
#             while right<n and matchingChr!=tChN:
#                 winFreq[s[right]] = winFreq.get(s[right],0)+1
#                 if s[right] in tFreq and winFreq[s[right]]==tFreq[s[right]]:
#                     matchingChr+=1
#                 right +=1

#             while matchingChr==tChN and left<right:
#                 winFreq[s[left]] -=1
#                 if s[left] in tFreq and winFreq[s[left]]==tFreq[s[left]]-1:
#                     matchingChr-=1
#                     if not minSubStr or len(minSubStr)> right-left:
#                         minSubStr = s[left: right]

#                 left +=1

#         return minSubStr if minSubStr else ""
