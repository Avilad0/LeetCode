# tc = O(logn), sc=O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0 or x==1:
            return x

        ans = 1
        if n<0:
            n*=(-1)
            x=1/x
        
        while n>0:
            if n%2==1:
                ans*=x
            
            x*=x
            n//=2
        
        return ans