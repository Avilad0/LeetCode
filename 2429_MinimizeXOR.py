#same as below but refactored duplicate code
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_set_bits, num2_set_bits = num1.bit_count(), num2.bit_count()
        i, x, bits_to_flip = 0, num1, abs(num1_set_bits-num2_set_bits)
        check = 1 if num1_set_bits>num2_set_bits else 0
        while bits_to_flip:
            if (x>>i) & 1 == check:
                bits_to_flip-=1
                x = x ^ (1<<i)
            i+=1
        return x


# class Solution:
#     def minimizeXor(self, num1: int, num2: int) -> int:
#         num1_set_bits, num2_set_bits = num1.bit_count(), num2.bit_count()
#         if num1_set_bits == num2_set_bits:
#             return num1
        

#         if num1_set_bits>num2_set_bits:
#             i, x = 0, num1

#             while num1_set_bits!=num2_set_bits:
#                 if (x>>i) & 1:
#                     num1_set_bits-=1
#                     x = x ^ (1<<i)
#                 i+=1
#             return x
#         else :
#             i, x = 0, num1
#             while num1_set_bits!=num2_set_bits:
#                 if (x>>i) & 1 == 0:
#                     num1_set_bits+=1
#                     x = x | (1<<i)
#                 i+=1
#             return x

#         return -1
    
print(Solution().minimizeXor(25, 72)) #24


num1 =25
num2 = 72
# write num1 and num2 in binary form
# num1 =   11001
# num2 = 1001000
# so the answer will be 24 = 11000