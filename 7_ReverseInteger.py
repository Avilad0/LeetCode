import math

#tc=O(1), sc=O(1)   #32 bit ints
class Solution:
    def reverse(self, x: int) -> int:
        maxInt = 0x7FFFFFFF
        maxIntDiv10 = maxInt//10
        maxIntMod10 = maxInt%10

        minInt = -maxInt-1
        minIntDiv10 = int(minInt/10)
        minIntMod10 = int(math.fmod(minInt,10))

        y=0
        while x:
            # use int of math.fmod instead of % for c++/java like mod calculations of negative numbers. 
            # eg. -18fmod10 =-8.0 vs -18%10=2
            lastDigit = int(math.fmod(x,10))
            # use int of / and not //.
            # eg: int(-18/10) = -1 vs -18//10=-2
            x=int(x/10)

            if y>maxIntDiv10 or (y==maxIntDiv10 and lastDigit>maxIntMod10):
                return 0
            if y<minIntDiv10 or (y==minIntDiv10 and lastDigit<minIntMod10):
                return 0
            
            y=y*10+lastDigit
        
        return y