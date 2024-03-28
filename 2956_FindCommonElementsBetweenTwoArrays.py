from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = [0]*100
        c2 = [0]*100

        for n in nums1:
            c1[n-1] = 1

        for n in nums2:
            c2[n-1] = 1
        
        ans1 = 0
        for n in nums1:
            if c2[n-1] == 1:
                ans1+=1

        ans2 = 0
        for n in nums2:
            if c1[n-1] == 1:
                ans2+=1

        return [ans1,ans2]