from typing import List
import heapq

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        minHeap, maxHeap = [(nums[0],0)], [(-nums[0],0)]

        n,i,j = len(nums), 0, 0
        ans = 0
        while j<n:
            prevj = j
            while - maxHeap[0][0] - minHeap[0][0]<=2:
                j+=1
                if j>=n:
                    break
                heapq.heappush(maxHeap, (-nums[j],j))
                heapq.heappush(minHeap, (nums[j],j))
            
            ans += ((j-i)*(j-i+1)//2) - ((prevj-i)*(prevj-i+1)//2)

            while i<j and - maxHeap[0][0] - minHeap[0][0]>2:
                while maxHeap[0][1]<=i:
                    heapq.heappop(maxHeap)
                while minHeap[0][1]<=i:
                    heapq.heappop(minHeap)
                i+=1
        
        return ans
    
print(Solution().continuousSubarrays(nums = [35,35,36,37,36,37,38,37,38])) # 21+ 28 - 10 = 39
print(Solution().continuousSubarrays(nums = [5,4,2,4])) # 8
print(Solution().continuousSubarrays(nums = [31,30,31,32])) # 10