class Solution:
    def reverse(self, x: int) -> int:
        mul = -1 if x<0 else 1
        ans = 0

        x*=mul
        while x!=0:
            r = x%10
            ans = ans*10 + r
            x=x//10

        m = 2**31
        if (mul==-1 and ans>m) or (mul==1 and ans>=m):
            return 0

        return ans*mul
    
print(Solution().reverse(-123))