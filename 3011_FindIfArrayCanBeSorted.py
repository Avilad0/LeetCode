from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        curr_bits = 0
        curr_maxx, prev_maxx = 0,0
        for num in nums:
            bits = num.bit_count()
            if num<prev_maxx:
                    return False
            elif bits!=curr_bits:
                if num<curr_maxx:
                     return False
                curr_bits = bits
                prev_maxx = curr_maxx
                curr_maxx = num
            elif num>curr_maxx:
                    curr_maxx = num

        return True
    

print(Solution().canSortArray([20,16]))  #False
# print(Solution().canSortArray([1,2,3,4,5])) #True