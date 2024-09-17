from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        words = Counter(s1.split()) + Counter(s2.split())
        
        uncommon = []
        for w,f in words.items():
            if f==1:
                uncommon.append(w)

        return uncommon


print(Solution().uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))




'''
a b c d
b c d e

a
e
'''