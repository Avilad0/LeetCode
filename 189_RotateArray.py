from typing import List

# sc = O(1), tc= O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start<end:
                nums[start],nums[end] = nums[end], nums[start]
                start, end = start+1, end-1

        n = len(nums)
        k = k%n
        reverse(0,n-k-1)
        reverse(n-k,n-1)
        reverse(0,n-1)

# # sc = O(n), tc= O(n)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         temp = [nums[(i-k+n)%n] for i in range(n)]

#         for i in range(n):
#             nums[i] = temp[i]
       


'''
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

1,2,3,4     5,6,7

4,3,2,1     7,6,5
5,6,7       1,2,3,4

5,6,7,1,2,3,4     

'''