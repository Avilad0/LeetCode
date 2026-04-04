class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        max_int = 0x7FFFFFFF
        if a<= max_int:
            return a

        # python negative ints has infinte preceding bits as 1. 
        # a^mask marks all significant bits in 32-bit a as 0.
        # ~ converts all these 0 to 1 again but also marks all preceding 0's with 1 and converts it to negative python form
        return ~(a ^ mask)