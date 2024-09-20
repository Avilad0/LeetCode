class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        reversed_string = s[::-1]

        for i in range(length):
            if s[: length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ""

'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if s==s[::-1]:
            return s
        
        sFreq = []
        prev = s[0]
        counter =1
        for c in s[1:]:
            if c==prev:
                counter+=1
            else:
                sFreq.append((prev, counter))
                prev = c
                counter =1
        
        sFreq.append((prev, counter))

        i = 0
        j= len(sFreq) -1
        jStart = -1
        toCheck = False

        while j >= 0:
            if sFreq[i][0]==sFreq[j][0] and (sFreq[i][1]==sFreq[j][1] or (i==0 and sFreq[i][1]<sFreq[j][1])):
                if not toCheck:
                    toCheck = True
                    jStart = j
                i+=1
                j-=1
                continue
            else:
                if toCheck:
                    j=jStart-1
                else:
                    j-=1
                i=0
                toCheck= False

        ans = ''
        for c in sFreq[: jStart: -1]:
            ans+= c[0]*c[1]

        # for c in sFreq[:jStart]:
        #     ans+= c[0]*c[1]
        
        return ans + s
'''

print(Solution().shortestPalindrome('aacecaaa'))  #aaacecaaa
# print(Solution().shortestPalindrome('abcd'))  #dcbabcd



'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]

        if s==rev_s:
            return s
        
        n= len(s)
        i=0
        j=0
        jStart = -1
        toCheck = False

        while j < n:
            if rev_s[j]==s[i]:
                if not toCheck:
                    toCheck = True
                    jStart = j
                i+=1
                j+=1
                continue
            else:
                if toCheck:
                    j=jStart+1
                else:
                    j+=1
                i=0
                toCheck= False
        
        return rev_s[:jStart] + s


'''

'''
abacd

abacd
bcaba


--
s = aacecaaa
r = aaacecaa

s = a2, c1, e1, c1, a3
r = a3, c1, e1, c1, a2

--
ans = acecaaceca
s = aaceca
r = acecaa

s = a2, c1, e1, c1, a1
r = a1, c1, e1, c1, a2

--

s = abacd
r = dcaba

s = a1, b1, a1, c1, d1
r = d1, c1, a1, b1, a1

--

s = abcd
r = dcba

s = a1, b1, c1, d1
r = d1, c1, b1, a1

'''