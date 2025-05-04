from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = defaultdict(int)
        pairs = 0
        for d in dominoes:
            if d[0]>d[1]:
                key = (d[1],d[0])
            else:
                key = (d[0], d[1])
            
            pairs+=freq[key]
            freq[key]+=1
        
        return pairs
                
            