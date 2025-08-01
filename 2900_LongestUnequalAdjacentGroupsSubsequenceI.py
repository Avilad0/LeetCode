from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        for i in range(1, len(groups)):
            if groups[i]!=groups[i-1]:
                ans.append(words[i])
        return ans