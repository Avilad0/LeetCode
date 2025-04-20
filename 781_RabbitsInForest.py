from collections import defaultdict
import math
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(int)
        for ans in answers:
            freq[ans]+=1
        
        rabbits = 0
        for ans, f in freq.items():
            rabbits += math.ceil(f/(ans+1))*(ans+1)

        return rabbits

'''
ans = [3,3,3,3,3,3,3]
f = [3:7]
rabbitsmin = 4,4 = 8

'''