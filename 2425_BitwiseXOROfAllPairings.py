from typing import List

#same as below but refactored
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0 

        if len(nums1)%2:
            for i in range(len(nums2)):
                ans^=nums2[i]
        
        if len(nums2)%2:
            for i in range(len(nums1)):
                ans^=nums1[i]

        return ans

# class Solution:
#     def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
#         n1, n2 = len(nums1), len(nums2)
#         if n1%2==0 and n2%2==0:
#             return 0
#         elif n1%2==1 and n2%2==1:
#             ans = 0
#             for i in range(n1):
#                 ans ^= nums1[i]
#             for i in range(n2):
#                 ans ^= nums2[i]
#             return ans
#         elif n1%2==0:
#             ans = 0
#             for i in range(n1):
#                 ans ^= nums1[i]
#             return ans

#         ans = 0
#         for i in range(n2):
#             ans ^= nums2[i]
#         return ans
    
'''
if both even = 0
if both odd = xor of all
else include the xor of array num2 if num1 is odd or vice versa
------------------------
nums1 = [a, b, c]
nums2 = [x,y]

nums3 = [ a^x, a^y, b^x,.... ]
nums3_Xor = a^x ^ a^y ^ b^x ^ b^y ^ c^x ^ c^y
----------------------

nums1 = [a, b]
nums2 = [x,y]

nums3 = [ a^x, a^y, b^x,.... ]
nums3_Xor = a^x ^ a^y ^ b^x ^ b^y  = 0

'''