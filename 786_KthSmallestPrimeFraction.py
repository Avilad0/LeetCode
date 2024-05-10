from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        # this is faster than 2nd solution, but 2nd is easier to implement and decode
        n = len(arr)
        left, right = 0, 1.0
        
        while left < right:
            mid = (left + right) / 2
            max_fraction = 0.0
            total_smaller_fractions = 0
            numerator_idx, denominator_idx = 0, 0

            j = 1            
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1

                total_smaller_fractions += (n - j)

                if j == n:
                    break

                fraction = arr[i] / arr[j]

                if fraction > max_fraction:
                    numerator_idx = i
                    denominator_idx = j
                    max_fraction = fraction

            if total_smaller_fractions == k:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif total_smaller_fractions > k:
                right = mid
            else:
                left = mid

        return []


        # heap = []
        # l = len(arr)

        # for i in range(0,l-1):
        #     heappush(heap, [arr[i]/arr[l-1], [i, l-1]])

        # while k>1:
        #     fraction = heappop(heap)[1]
        #     fraction[1] -=1
        #     heappush(heap, [arr[fraction[0]] / arr[fraction[1]], fraction])
        #     k-=1

        # fraction = heappop(heap)[1]
        # return [arr[fraction[0]], arr[fraction[1]]]

        

    
print(Solution().kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3))
print(Solution().kthSmallestPrimeFraction(arr = [1,7], k = 1))
print(Solution().kthSmallestPrimeFraction(arr = [1,13,17,59], k = 6))
