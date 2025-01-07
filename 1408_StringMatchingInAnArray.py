from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = set()
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if words[i].__contains__(words[j]):
                        ans.add(words[j])
        
        return list(ans)