from collections import defaultdict
from typing import List

class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n<10:
            return n
        
        sumFreq = defaultdict(int)
        maxFreq = 0
        count = 0
        for i in range(1,n+1):
            curSum = 0
            while i>0:
                curSum+= (i%10)
                i//=10
            sumFreq[curSum]+=1
            if sumFreq[curSum] > maxFreq:
                maxFreq = sumFreq[curSum]
                count = 1
            elif sumFreq[curSum] == maxFreq:
                count+=1

        return count



'''
1 10
2 11 20
3 12 21 30
4 13 22 31
5 14 23 32
6 15 24 33
7 16 25 34
8 17 26 35
9 18 27 36
  19 28 37
     29 38
        39
'''