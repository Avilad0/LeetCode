from typing import List

'''
example : count(10) = count(0b1010) = (count("1") + count("010")) or (count("101") + count("0") )
'''

# tc = O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1,n+1):
            ans.append(ans[i>>1] + (i&1))

        return ans
    

# # tc = O(n)
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         ans = [0]
#         valOfMostSignificantBit = 1
#         for i in range(1,n+1):
#             if i==2*valOfMostSignificantBit:
#                 valOfMostSignificantBit=i

#             ans.append(1+ ans[i-valOfMostSignificantBit])
#         return ans
    

    
# # tc = O(nlogn)
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         ans = []
#         for num in range(n+1):
#             curr, count = num, 0
#             while curr:
#                 count += curr&1
#                 curr >>=1
#             ans.append(count)
        
#         return ans
