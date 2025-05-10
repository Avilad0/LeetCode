from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0,0
        zeros1, zeros2 = 0,0

        for num in nums1:
            if num==0:
                zeros1+=1
            else:
                sum1+=num
        
        for num in nums2:
            if num==0:
                zeros2+=1
            else:
                sum2+=num

        if zeros1==0 and zeros2==0:
            if sum1==sum2:
                return sum1
            else:
                return -1
        elif zeros1==0:
            if sum1>=(sum2+zeros2):
                return sum1
            else:
                return -1
        elif zeros2==0:
            if (sum1+zeros1)<=sum2:
                return sum2
            else:
                return -1

        return max(sum1+zeros1, sum2+zeros2)