class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = int(1e9 + 7)

        def power(base, exponent)->int:
            ans = 1
            while exponent:
                if exponent%2:
                    ans = (ans*base)%MOD
                
                base = (base*base)%MOD
                exponent//=2
            
            return ans
        
        ans = power(20, n//2)
        if n%2:
            ans = (ans*5)%MOD

        return ans

        # #even places * odd places
        # return (power(5, (n+1)//2) * power(4, n//2) )%MOD
    

'''
n= 5
odds = 2 = n//2
evens = 3 = (n+1)//2

n=6
odds = 3 = n//2
evens = 3 = (n+1)//2

5**evens * 4**odds

if n is odd:
    20**odds
else:
    20**odds  * 5
'''