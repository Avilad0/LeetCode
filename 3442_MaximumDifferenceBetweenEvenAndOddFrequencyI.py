from collections import defaultdict

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[c]+=1
        
        maxOdd, minEven = 0,float('inf')

        for f in freq.values():
            if f%2:
                if f>maxOdd:
                    maxOdd = f
            else:
                if f<minEven:
                    minEven = f

        return maxOdd - minEven