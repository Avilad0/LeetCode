
# tc = O(logn), but since n<=2^32, tc=O(32)=O(1)
# Using bit-operatrions
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            bits += n&1
            n>>=1
        
        return bits
    

# Using arithmetic-operatrions (same comoplexity)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         bits = 0
#         while n:
#             bits += n%2
#             n//=2
        
#         return bits