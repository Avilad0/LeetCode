from typing import List


# tc=O(n), sc=O(n) - using deque
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n= len(nums)
        ans = []

        left=0
        q = deque([])
        
        for right in range(n):
            while q and nums[right]>=nums[q[-1]]:
                q.pop()
            
            q.append(right)

            if q[0]<left:
                q.popleft()

            if right>=k-1:
                ans.append(nums[q[0]])
                left+=1
        
        return ans



# # tc=O(nlogn), sc=O(n) - using heap (or maybe nlogk because of emptying heaps conditionally)
# import heapq
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         heap = [] # maxHeap - (-val, index)
#         n = len(nums)

#         for i in range(k):
#             if heap and -heap[0][0]<=nums[i]:
#                 heap = []

#             heapq.heappush(heap, (-nums[i], i))
        
#         ans = [-heap[0][0]]

#         for i in range(k,n):
#             if heap and -heap[0][0]<=nums[i]:
#                 heap = []

#             while heap and heap[0][1]<=i-k:
#                 heapq.heappop(heap)
            
#             heapq.heappush(heap, (-nums[i], i))
#             ans.append(-heap[0][0])
        
#         return ans