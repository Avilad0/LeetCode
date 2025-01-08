from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count, n = 0, len(words)
        for i in range(n-1):
            for j in range(i+1,n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1

        return count