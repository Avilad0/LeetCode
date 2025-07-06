from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1Freq = Counter(nums1)
        self.nums2Freq = Counter(nums2)
        self.nums2 = nums2
        

    def add(self, index: int, val: int) -> None:
        self.nums2Freq[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.nums2Freq[self.nums2[index]]+=1

    def count(self, tot: int) -> int:
        ans = 0
        for num1, f in self.nums1Freq.items():
            if tot-num1 in self.nums2Freq:
                ans+=self.nums2Freq[tot-num1]*f
        
        return ans

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)