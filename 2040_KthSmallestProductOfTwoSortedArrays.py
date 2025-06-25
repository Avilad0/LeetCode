from typing import List
from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)

        def isMoreThanKSatisfied(product):
            totalSatisfied = 0
            for num1 in nums1:
                if num1>0:
                    totalSatisfied +=  bisect_right(nums2, product//num1)
                elif num1<0:
                    totalSatisfied += n2 - bisect_left(nums2, -(-product//num1))
                else:
                    if product>=0:
                        totalSatisfied+=n2
            
            return totalSatisfied>=k


        left, right = min(nums1[0]*nums2[0], nums1[-1]*nums2[-1], nums1[0]*nums2[-1], nums1[-1]*nums2[0]), max(nums1[0]*nums2[0], nums1[-1]*nums2[-1], nums1[0]*nums2[-1], nums1[-1]*nums2[0])

        while left<right:
            mid = (left+right)//2
            if isMoreThanKSatisfied(mid):
                right = mid
            else:
                left = mid+1

        return right


print(Solution().kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6)) #0
print(Solution().kthSmallestProduct(nums1 = [-9,-4,1,6,8,8,9,10], nums2 = [-10,-10,-8,-8,1,3,6,6,8,10], k = 29)) #-24


'''
nums1 = [-2,-1,0,1,2] 
nums2 = [-3,-1,2,4,5]

-2 5
-2 4
-1 5
-1 4
-2 2
-1 2
 0 5
 0 4
 0 2

-3 2
-3 1
-1 2
-1 1



'''