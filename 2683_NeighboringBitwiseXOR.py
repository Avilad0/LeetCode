from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived)%2==0

'''
1110
0010  x
1010  x

0001
0011  x
1111  x
1110

111
010   x

derived = [a,b,c]
original = [x,y,z]
a^b^c = x^y^y^z^z^x = 0
'''

# space O(n) and time O(n)
# class Solution:
#     def doesValidArrayExist(self, derived: List[int]) -> bool:
#         # Create an original array initialized with 0.
#         original = [0]
#         for i in range(len(derived)):
#             original.append(derived[i] ^ original[i])

#         # Store the validation results in checkForZero and checkForOne respectively.
#         check_for_zero = original[0] == original[-1]
#         original = [1]
#         for i in range(len(derived)):
#             original.append(derived[i] ^ original[i])
#         check_for_one = original[0] == original[-1]

#         return check_for_zero or check_for_one