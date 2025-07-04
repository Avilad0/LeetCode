from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        additions = 0
        while k != 1: 
            # let k = 2**t + x.  if x==0,  then prevK (k depends On) = k - 2**(t-1), else prevK (k depends On) = k - 2**t = x
            t = k.bit_length() - 1  
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]==1:
                additions += 1

        return chr(ord("a") + (additions%26))
    

'''

Input: k = 10, operations = [0,1,0,1]

Output: "b"

a                       \\ newK = 1
a"a"                    \\ newK = 2 = 0b10 = 2**1 + 0  \\ 1st pos in operation (1-1 = 0th index) \\ ans += 0 \\ newK = 2-1 = 1
a"a"bb
a"a"bbaabb                
aabbaabbb"b"ccbbcc      \\ k=10 = 0b1010 = 2**3 + 2 \\ 3rd in operation (3rd index) \\ ans +=1 \\ newK = 10-8 = 2 (remove first set bit ,  go to previous half in str)

total additions 1 = 'a'+1 ='b' 
'''