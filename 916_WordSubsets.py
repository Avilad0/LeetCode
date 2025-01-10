from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_freq = [0]*26
        for word in words2:
            t = [0]*26
            for c in word:
                t[ord(c)-97]+=1
            
            for i in range(26):
                if t[i]>words2_freq[i]:
                    words2_freq[i] = t[i]
        
        universal_str = []
        for word in words1:
            t = [0]*26
            for c in word:    
                t[ord(c)-97]+=1
            
            is_subset = True
            for i in range(26):
                if t[i]<words2_freq[i]:
                    is_subset = False
                    break

            if is_subset:
                universal_str.append(word)
        
        return universal_str
    
print(Solution().wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))   # Output: ["facebook","google","leetcode"]