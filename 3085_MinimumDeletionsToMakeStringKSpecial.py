from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = defaultdict(int)
        for c in word:
            freq[c]+=1
        
        freqVals = freq.values()
        minDeletes = len(word)

        for val1 in freqVals:
            deletion = 0
            for val2 in freqVals:
                if val1>val2:
                    deletion+=val2
                elif val1+k<val2:
                    deletion += val2-val1-k
            
            if minDeletes>deletion:
                minDeletes = deletion

        return minDeletes



# from collections import defaultdict

# class Solution:
#     def minimumDeletions(self, word: str, k: int) -> int:
#         freq = defaultdict(int)
#         for c in word:
#             freq[c]+=1
        
#         sortedFreq = sorted(freq.values())
#         n, nf = len(word), len(sortedFreq)
#         minDeletes = n

#         for i in range(nf):
#             used = 0
#             for j in range(i,nf):
#                 used += sortedFreq[j] - max(0, sortedFreq[j]- sortedFreq[i]-k)
            
#             minDeletes = min(minDeletes, n-used)

#         return minDeletes

        
            


# from collections import defaultdict
# from functools import cache

# class Solution:
#     def minimumDeletions(self, word: str, k: int) -> int:
#         freq = defaultdict(int)
#         for c in word:
#             freq[c]+=1
        
#         sortedFreq = sorted(freq.values())
#         n, nf = len(word), len(sortedFreq)

#         @cache
#         def dfs(i, used, minF):
#             if i==nf:
#                 return 0
            
#             deletions = used + dfs(i+1, sortedFreq[i], sortedFreq[i])

#             if minF!=-1:
#                 deletions = min(deletions, max(0,sortedFreq[i]-minF-k) + dfs(i+1, used + sortedFreq[i], minF))
            
#             return deletions

#         return dfs(0,0,-1)
            
    
    
    
print(Solution().minimumDeletions( word = "aabcaba", k = 0))