from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < n and arr[left] > arr[right]:
                right += 1
            if right-left-1<ans:
                ans = right - left - 1
            left += 1
        return ans


# print(Solution().findLengthOfShortestSubarray(arr = [1,2,3])) #0
print(Solution().findLengthOfShortestSubarray(arr = [1,2,3,10,0,7,8,9])) #2