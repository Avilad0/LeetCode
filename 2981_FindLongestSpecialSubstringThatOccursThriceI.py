class Solution:
    def maximumLength(self, s: str) -> int:
        count  = [[0]*3 for _ in range(26)]

        prev = 0
        i, n = 1, len(s)
        while i<n:
            while i<n and s[i]==s[prev]:
                i+=1
            
            index = ord(s[prev])-97
            j=0
            while j<3 and count[index][j] >= i-prev:
                j+=1
            if j<3:
                count[index].insert(j, i-prev)
                count[index].pop()
            
            prev = i

        ans = -1
        for x in count:
            ans = max(ans, x[0]-2)
            if x[2]>0:
                ans = max(ans, x[2])
            if x[1]>0:
                if x[1]==x[0]:
                    ans = max(ans, x[1]-1)
                else:
                    ans = max(ans, x[1])
                
        
        return -1 if ans<1 else ans
    

# print(Solution().maximumLength(s = "abcaba")) #Output: 1
# print(Solution().maximumLength(s = "aaaa")) #Output: 2
# print(Solution().maximumLength('eccdnmcnkl')) #Output: 1
print(Solution().maximumLength(s = "eeeyyyybbbbbbbbssppb")) #Output: 6
