class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2147483648 and divisor==-1:
            return 2147483647

        flag =1
        if (dividend<0) ^ (divisor<0):
            flag=-1

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0
    
        while divisor <= dividend:
            shift = 0
            while (divisor<<shift) <= dividend:
                shift+=1

            ans += (1<<(shift-1))

            dividend-= divisor<<(shift-1)
            
        return ans*flag


print(Solution().divide(-2147483648,-1))