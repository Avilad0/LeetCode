from typing import List

# # tc=O( log(min(m,n)) ), sc=O(1) - binary search over shorter array and partitioning correctly to get middle elements
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        if m>n:
            nums1, nums2 = nums2, nums1
            m,n = n,m

        left, right = 0, m  #use m and not m-1 because we can have all elements of nums1 in left half
        while left<=right:
            partition1 = (left+right)//2  # number of elements part of left smaller half of nums1
            partition2 = (m+n+1)//2 - partition1 # number of elements in nums2 so as to divide combined arrays into equal number of smaller and bigger members
            # use (m+n+1)//2 as ceil of middle of total nums so 1 extra element will be on left in case of odd and 1 on each side in case of even total length

            maxLeft1 = float('-inf') if partition1==0 else nums1[partition1-1]
            minRight1 = float('inf') if partition1==m else nums1[partition1]
            maxLeft2 = float('-inf') if partition2==0 else nums2[partition2-1]
            minRight2 = float('inf') if partition2==n else nums2[partition2]

            # check if left1 has all lower values than right2 and left2 has all lower values than right1, then partition gives us middle 4 values in merged sorted list
            if maxLeft1<=minRight2 and maxLeft2<=minRight1:
                
                if (m+n)%2==0:
                    return (max(maxLeft1,maxLeft2) + min(minRight1, minRight2))/2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1>minRight2:
                right=partition1-1
            else:
                left=partition1+1

        return None #will not reach here


'''
m,n=6,7
partition1,partition2 = 3, 4
7 on left and 6 on right

m,n=6,8
partition1,partition2 = 3, 4
7 on left and 7 on right
'''

# # tc=O(m*n), sc=O(1) - 2 pointers - same as below but cleaner code
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m,n = len(nums1), len(nums2)
#         p1, p2 = 0,0

#         def getMin():
#             nonlocal p1,p2
#             if p1==m:
#                 p2+=1
#                 return nums2[p2-1]
#             elif p2==n:
#                 p1+=1
#                 return nums1[p1-1]
#             elif nums1[p1]<=nums2[p2]:
#                 p1+=1
#                 return nums1[p1-1]
#             else:
#                 p2+=1
#                 return nums2[p2-1]
        
#         for i in range((m+n-1)//2):
#             getMin()

#         if (m+n)%2==0:
#             return (getMin() + getMin())/2
#         return getMin()
    


# # tc=O(m*n), sc=O(1) - 2 pointers
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m,n = len(nums1), len(nums2)
#         p1, p2 = 0,0
        
#         for i in range((m+n-1)//2):
#             if p1==m:
#                 p2+=1
#             elif p2==n:
#                 p1+=1
#             elif nums1[p1]<=nums2[p2]:
#                 p1+=1
#             else:
#                 p2+=1
        
#         if (m+n)%2==0:
#             if p1==m:
#                 return (nums2[p2]+nums2[p2+1])/2
#             elif p2==n:
#                 return (nums1[p1]+nums1[p1+1])/2
#             elif nums1[p1]<=nums2[p2]:
#                 median1 = nums1[p1]
#                 median2 = min( float("inf") if p1+1==m else nums1[p1+1], float("inf") if p2==n else nums2[p2] )
#                 return (median1+median2)/2
#             else:
#                 median1 = nums2[p2]
#                 median2 = min( float("inf") if p1==m else nums1[p1], float("inf") if p2+1==n else nums2[p2+1] )
#                 return (median1+median2)/2
            
        
#         return min( float("inf") if p1==m else nums1[p1], float("inf") if p2==n else nums2[p2] )