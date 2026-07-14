class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n=len(digits)
        i, carry=n-1, 1
        while i>=0 and carry>0:
            summ = digits[i]+carry
            digits[i], carry = summ%10, summ//10
            i-=1
        
        if carry>0:
            # return [carry]+digits #causes O(n) extra space
            digits.reverse()
            digits.append(carry)
            digits.reverse()
        
        return digits